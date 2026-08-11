#!/usr/bin/env python3
"""
extract_docx_comments.py — Extract review comments from a .docx file into
clean Markdown, anchored to the text they were left on.

Part of the qira-assessor skill's review workflow: when a colleague annotates
a Recording Form (.docx) in Word/SharePoint and you get it back, run this to
pull every comment out into a Markdown file suitable for committing to the
repo's outputs/ folder alongside the original assessment.

Usage:
    python3 extract_docx_comments.py reviewed.docx -o comments.md
    python3 extract_docx_comments.py reviewed.docx          # prints to stdout

Handles: top-level comments, threaded replies (nested under their parent),
multiple comments anchored to the same or overlapping text, and comments
with no resolvable anchor (falls back to "(anchor text not found)").

No third-party dependencies — stdlib zipfile + xml.etree only.
"""

import argparse
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
W15 = "{http://schemas.microsoft.com/office/word/2012/wordml}"


def _text_of(elem):
    """Concatenate all w:t descendant text under elem."""
    return "".join(t.text or "" for t in elem.iter(f"{W}t"))


def _load_xml(docx_path, part):
    with zipfile.ZipFile(docx_path) as z:
        names = z.namelist()
        if part not in names:
            return None
        with z.open(part) as f:
            return ET.parse(f).getroot()


def _parse_comments(comments_root):
    """Return {comment_id: {"author", "date", "text", "parent_id"}}."""
    comments = {}
    if comments_root is None:
        return comments
    for c in comments_root.findall(f"{W}comment"):
        cid = c.get(f"{W}id")
        comments[cid] = {
            "author": c.get(f"{W}author") or "(unknown)",
            "date": c.get(f"{W}date") or "",
            "text": _text_of(c).strip(),
            "parent_id": None,
        }
    return comments


def _parse_extended(comments_extended_root, comments):
    """commentsExtended.xml carries parent/reply linkage via paraId, not
    comment id directly — map paraId -> comment id first, then set parent_id."""
    if comments_extended_root is None:
        return
    # Build paraId -> comment id map by re-walking comments.xml structure
    # (commentsExtended references w15:paraId of the comment's own paragraph)
    para_to_cid = {}
    # We need the original comments.xml root again for paraId lookup;
    # caller passes comments already keyed by id but not paraId, so this
    # mapping is best-effort and only used if present.
    for ex in comments_extended_root.findall(f"{W15}commentEx"):
        pass  # paraId-based linkage is best-effort; see NOTE below.


def _find_anchors(document_root):
    """
    Walk word/document.xml and, for each commentRangeStart/End pair, capture
    the plain text between them. Returns {comment_id: anchor_text}.
    Handles nested ranges (reply comments sharing a parent's anchor).
    """
    anchors = {}
    open_ranges = {}  # id -> list of text fragments accumulated so far

    # We need document order, so iterate the full tree in sequence.
    for elem in document_root.iter():
        tag = elem.tag
        if tag == f"{W}commentRangeStart":
            cid = elem.get(f"{W}id")
            open_ranges[cid] = []
        elif tag == f"{W}commentRangeEnd":
            cid = elem.get(f"{W}id")
            if cid in open_ranges:
                anchors[cid] = "".join(open_ranges.pop(cid)).strip()
        elif tag == f"{W}t" and open_ranges:
            frag = elem.text or ""
            for cid in open_ranges:
                open_ranges[cid].append(frag)

    return anchors


def extract(docx_path):
    comments_root = _load_xml(docx_path, "word/comments.xml")
    document_root = _load_xml(docx_path, "word/document.xml")
    extended_root = _load_xml(docx_path, "word/commentsExtended.xml")

    comments = _parse_comments(comments_root)
    if document_root is not None:
        anchors = _find_anchors(document_root)
        for cid, text in anchors.items():
            if cid in comments:
                comments[cid]["anchor"] = text
    for c in comments.values():
        c.setdefault("anchor", "(anchor text not found)")

    # Reply threading: commentsExtended.xml links replies to parents via
    # w15:paraIdParent, matched against each comment's own w14:paraId.
    # Re-parse comments.xml directly for paraId, since _parse_comments()
    # doesn't retain it.
    paraid_to_cid = {}
    if comments_root is not None:
        for c in comments_root.findall(f"{W}comment"):
            cid = c.get(f"{W}id")
            p = c.find(f"{W}p")
            if p is not None:
                paraid = p.get("{http://schemas.microsoft.com/office/word/2010/wordml}paraId")
                if paraid:
                    paraid_to_cid[paraid] = cid

    if extended_root is not None:
        for ex in extended_root.findall(f"{W15}commentEx"):
            para_id = ex.get(f"{W15}paraId")
            parent_paraid = ex.get(f"{W15}paraIdParent")
            cid = paraid_to_cid.get(para_id)
            parent_cid = paraid_to_cid.get(parent_paraid) if parent_paraid else None
            if cid in comments and parent_cid:
                comments[cid]["parent_id"] = parent_cid

    return comments


def to_markdown(comments, source_name):
    if not comments:
        return f"# Review comments — {source_name}\n\nNo comments found in this document.\n"

    # Group by top-level comment, threading replies beneath their parent,
    # in id order (Word assigns ids roughly in insertion order).
    top_level = [cid for cid, c in comments.items() if not c["parent_id"]]
    top_level.sort(key=lambda x: int(x) if x.isdigit() else 0)

    lines = [f"# Review comments — {source_name}", ""]
    lines.append(f"Extracted {len(comments)} comment(s).")
    lines.append("")

    def render(cid, depth=0):
        c = comments[cid]
        indent = "  " * depth
        prefix = "-" if depth == 0 else "  " + "-"
        lines.append(f"{indent}**{c['author']}**{' (reply)' if depth else ''} — {c['date']}")
        if depth == 0:
            lines.append(f"{indent}> Anchored text: \"{c['anchor']}\"")
        lines.append(f"{indent}> {c['text']}")
        lines.append("")
        children = [k for k, v in comments.items() if v["parent_id"] == cid]
        children.sort(key=lambda x: int(x) if x.isdigit() else 0)
        for child in children:
            render(child, depth + 1)

    for cid in top_level:
        render(cid)

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", help="Path to the commented .docx file")
    ap.add_argument("-o", "--output", help="Write Markdown to this path (default: stdout)")
    args = ap.parse_args()

    comments = extract(args.docx)
    md = to_markdown(comments, args.docx.split("/")[-1])

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote {len(comments)} comment(s) to {args.output}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
