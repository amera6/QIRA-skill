# Changelog — qira-assessor

All notable changes to the `qira-assessor` skill since the first commit (2026-07-12). Dates are approximate, reconstructed from working-session history rather than commit metadata — cross-check against your own repo history if exact dates matter.

This file lives at the repo root, alongside `README.md` — not inside the `qira-assessor/` skill folder itself, consistent with the skill packaging convention (no extraneous files inside the folder Claude loads).

## [1.2.0] — Unreleased (pending push)

### Added
- **`scripts/extract_docx_comments.py`** — new script (no third-party dependencies; stdlib `zipfile` + `xml.etree` only) that parses a commented `.docx` and extracts every comment's author, date, anchored text, comment body, and threaded replies into clean Markdown. Built and tested against a real annotated test file (two top-level comments with distinct anchors) before being added to the skill. First component in the skill to require a Python environment — everything else remains pure Markdown reasoning.
- **Step 15 — Export a standalone Markdown file (on request)**, in `SKILL.md`. Formalizes producing a Recording Form as a standalone `.md` file (named after the Assessment reference) for committing to a repo's `outputs/` folder, separate from the conversational chat output.
- **Step 16 — Extract reviewer comments from an annotated Word document (on request)**, in `SKILL.md`. Documents the `extract_docx_comments.py` workflow: an on-demand step triggered whenever the analyst supplies a commented file, not a live sync against SharePoint or any other source.
- **`push_qira_output.sh`** (repo root, not part of the skill folder) — a local helper script for Git Bash that pulls, copies a file into `outputs/`, commits, and pushes. Intentionally kept outside the skill and outside anything Claude executes directly — it runs on the analyst's own machine using their own authenticated git setup, since the skill and Claude sessions should not handle GitHub credentials or tokens.

### Changed
- `compatibility` frontmatter field updated to note the one optional Python dependency (`extract_docx_comments.py`); trimmed to fit the 500-character frontmatter limit after the first draft exceeded it.
- Reading order in `SKILL.md` extended to include `scripts/extract_docx_comments.py`, flagged as Step-16-only, not needed for a standard assessment run.
- Version bumped `1.1.0` → `1.2.0`.

### Explicitly out of scope for this change (by design, not oversight)
- No automatic/passive monitoring of SharePoint for new comments — would require Power Automate or similar running on the analyst's infrastructure, outside what a Claude session can do on its own.
- No direct GitHub push from within a Claude session — no GitHub connector was available, and even if one were, Claude should not handle personal access tokens or other credentials directly. Pushing remains a locally-run, analyst-authenticated step.
- No direct SharePoint upload — the one relevant connector found (Microsoft 365) exposes search/read tools only, not a write/upload capability.

---

## [1.1.0] — 2026-07-30

### Added
- **IHR (2005) Annex 2 decision instrument** — new `references/ihr_annex2_decision_instrument.md`, grounded in the primary WHO guidance document (WHO/HSE/IHR/2010.4) and the consolidated IHR text. Covers the two notification categories (four always-notifiable diseases; the broader four-criteria assessment), the full criteria, and brief paraphrased case examples. Wired into `SKILL.md` Step 11, the footnote (i) reference in `references/risk_classification_and_actions.md`, and `references/algorithm_essentials.md` §7 — previously this check relied on unexamined background knowledge rather than a grounded source.
- **"Two kinds of interpretation" principle** — new critical section in `SKILL.md`, distinguishing (1) explaining the algorithm's own design/rationale, where the skill must stick to what the manual explicitly states and flag anything beyond that as synthesis, from (2) coding sub-questions against a specific signal, where judgment and interpretation are expected and should be reasoned openly. Prevents the skill from either fabricating design rationale or over-hedging on legitimate signal-coding judgment.
- **Citation-verification requirement** — new critical section in `SKILL.md` requiring that any specific fact, statistic, or claim in a Rationale needs a traceable, hyperlinked source: freshly searched and verified for genuinely external evidence, or linked back to the signal's own listed source when restating a signal-derived figure. Closes a real gap where earlier assessments stated plausible-sounding claims (e.g., historical comparator cases) without verification.
- **Confirmation-checklist flagging convention** — `SKILL.md` Step 12 now specifies a two-part convention for Hybrid/Interactive confirmation pauses: inline `CONFIRM:` tags at the point a judgment call is made, consolidated into a numbered, quote-anchored checklist before finalizing output. (Originally used an emoji marker; see Fixed, below.)
- **Metadata block and original-signal preservation** — `assets/recording_form_blank.md` now opens with an Assessment reference / Model / Date / Version block and a verbatim "Original signal" code block, preserved from Step 3 through to Step 13. The Assessment reference is explicitly documented as a human-readable labeling convention, not a real backend session ID (no tool exposes one).

### Changed
- **Part B table format**, twice:
  1. First restructured from a single domain-level row to one row *per sub-question* (A/B/C/D/E) plus a bolded Overall row per domain — intended to surface full reasoning, but produced excessively long tables (~19 rows per assessment).
  2. Consolidated back to one row per domain/question actually reached, with columns `Domain | Overall Question | Answer | Rationale` — full domain names and full question text in their own columns, with influential sub-questions named and described in prose within Rationale rather than broken into separate rows.
- **Citation scope broadened** — initially limited to "genuinely external" evidence only; broadened so that signal-derived figures restated in a Rationale cell also require a citation, back to the signal's own source, rather than being treated as citation-exempt. Goal: a fully traceable chain of evidence rather than a signal/external distinction.
- **Version metadata** bumped from `1.0.0` to `1.1.0` to reflect the accumulated changes in this file.

### Fixed
- **Emoji removed** from the Step 12 flagging convention (a magnifying-glass emoji in the original `CONFIRM:` marker), replaced with a plain bold text marker — per standing no-emoji preference.

---

## [1.0.0] — 2026-07-12 (first commit)

Initial public version of the skill, covering:
- Core `SKILL.md` with 14-step procedure and Autonomous/Hybrid/Interactive mode selector.
- `references/algorithm_essentials.md`, `domains_and_questions.md`, `risk_classification_and_actions.md`, `recording_form_template.md`, `worked_example.md`.
- `assets/recording_form_blank.md` (fillable output template) and `assets/qira_decision_tree.md` (Mermaid visual of the routing logic).
- Explicitly decoupled from MS-RRA — no dependency on or comparison to the MS-RRA framework, unlike the fifa-rra-assessor skill it was informally modeled alongside.
- A routing bug affecting Question 5.2 (five distinct capacity gates originally collapsed into one row in the consolidated routing table, silently producing wrong terminal risk levels for several paths) was caught during initial testing and fixed in `references/domains_and_questions.md` and `references/recording_form_template.md` before this commit — noted here since it's foundational to every subsequent assessment's correctness.
- `compatibility` and `metadata` (author, version, tested-against) fields added to frontmatter, following Anthropic's skill-building guide.
- Packaged as `qira-assessor.skill` via the skill-creator tooling's `package_skill.py`.

---

## Not yet part of the skill (flagged, not forgotten)

Two things introduced as one-off additions to individual output documents, not yet formalized into the skill's own files:
- A **sub-question reference appendix** (full text of every A/B/C/D/E sub-question, organized by domain) appended to exported Word documents.
- A **"Note from Claude"** block surfacing judgment-call commentary at the end of an assessment, on request.

If you want either to appear automatically on every Recording Form going forward, that needs a follow-up change to `assets/recording_form_blank.md`, `references/recording_form_template.md`, and `SKILL.md` Step 13/14 — not done yet.

## Known open items (from prior review, still outstanding)
- Gate **5.2c** is now exercised (Legionnaires' signal), but coverage of the full routing table across real test signals is worth re-auditing as a whole.
- **Domain 1 default-list heuristic** — informal practice of treating IHR Annex 2's four always-notifiable diseases as a stand-in high-threat list is not written into `algorithm_essentials.md` as a formal exception. Still an inconsistency between documented default (No, absent a supplied list) and actual practice for some signals.
- **C1 override selection criteria**, **Domain 3 comparison baselines**, **Domain 4 "unusual"/"significant" quantification**, and **Domain 5 B5 surveillance-as-capacity-proxy heuristic** remain undocumented judgment patterns — see prior session notes for detail.
