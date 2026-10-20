# QIRA — Evaluation Form Output Guide

**Companion to**: `qira-assessor` SKILL.md. Read at Step 13 whenever the Evaluation Form output format is requested, and use `assets/evaluation_form_blank.md` as the literal output structure.

**Source**: the analyst's *QIRA Skill Evaluation* document, Part 1. This output format exists to mirror that page so a human reviewer's independently-completed Part 1 and the skill's own answers sit side by side, question for question.

---

## Table of contents
1. What this format is for, and what it is not
2. Header block
3. Section 1 — Signal
4. Section 2 — Decision path table
5. Section 3 — Result
6. Section 4 — Proposed actions
7. Section 5 — Other considerations
8. Questions the routing bypassed
9. The aggregation notes in the domain rows
10. Relationship to the Results Recording Form

---

## 1. What this format is for, and what it is not

The document is titled **QIRA Claude Skill Results**. It records what the skill answered and why, one question at a time, in the same order and with the same lettering as the reviewer's own form. The reviewer completes their copy independently first, then reads this and compares.

Everything that makes the comparison work follows from one property: **question-for-question and label-for-label alignment with the reviewer's form.** A row that has been helpfully merged, reordered, or re-lettered is a row the reviewer has to translate before they can compare it. Sub-question lettering needs no translation — this skill letters sub-questions the way the reviewer's form does, per `domains_and_questions.md` §0 — so a coding made during the walk transfers straight into these cells.

**This document contains Part 1 material only.** Reviewers hold their own copy of the evaluation section (agreement, component ratings, points of divergence, factual errors, overall judgement), so it is not reproduced here — and never drafted, previewed, or pre-filled, since it is their assessment of this skill's performance.

**No instructional preamble.** The document opens with the title and goes straight to the header block. Do not add a line telling the reviewer when to complete the form; they are working from their own copy and already know the protocol.

## 2. Header block

| Field | Fill |
|---|---|
| Assessment ref. | The same reference used for the Recording Form (`QIRA-{jurisdiction}-{YYYY-MM-DD}-{hazard}-v{n}`), so the two artifacts pair unambiguously. |
| Date | Date of the QIRA run. |
| Area of interest / scoped population | The Step 3 scope, stated in the same words as the Recording Form's Scope line, with the forward-looking window. This is the unit of assessment every case count below is denominated in, so it must not drift between the two documents. |
| Assumption applied | Exactly one of: None (event domestic), Importation assumed, Spillover assumed. This must match what Step 3 established — an importation or spillover assumption is what every downstream answer is conditioned on, and a reader who misses it will compare against the wrong walk entirely. |

The header carries no reviewer-owned fields. This is the skill's results document, and blank boxes for a reviewer's name or elapsed time on it invite someone to fill them here instead of on their own form.

## 3. Section 1 — Signal

The analyst's original signal text, verbatim and unedited, preserved from Step 3 — the same text that goes in the Recording Form's Original signal block. **Keep any links live** as Markdown hyperlinks; the reviewer consults these sources while completing their own Part 1, so stripping them to plain text removes the evidence base they were given.

If the signal arrived across several messages or was refined mid-conversation, use the final complete version as actually assessed.

## 4. Section 2 — Decision path table

Four columns and **two kinds of row**. This structure exists to solve one specific complaint: in the earlier layout every sub-answer sat in one cell and every rationale in another, so a reader had to count down both to find out which fragment justified which answer. Here each sub-question's answer sits beside its own rationale, and nothing needs cross-referencing.

**Domain row** — shaded, one per domain or question reached:

| Column | Fill |
|---|---|
| Domain | The domain label with its conditional note, as printed: `Q3 Severity (only if Q2 = Y/U)`. The conditionals tell a reader which questions apply; keep them on rows that were reached. |
| Questions | The overall question text in full. |
| Answer | The main answer, in words and bold: **YES**, **NO**, **UNKNOWN**. |
| Sub-questions and rationale | The aggregation/routing rule in italics, reproduced unchanged. For Q4.1 and Q4.2 the comparator statement goes here too, beneath the rule (see below). |

**Sub-question rows** — one per guiding question, immediately beneath their domain row:

| Column | Fill |
|---|---|
| Domain | Empty. The domain row above already carries it; repeating it adds noise to a column a reader scans vertically. |
| Questions | The letter and the sub-question text, in bold: **A. Hazard still present?** |
| Answer | That sub-question's own answer, in words and bold. |
| Sub-questions and rationale | The rationale for *this* sub-question only. Fragments, not paragraphs; every specific fact hyperlinked. |

Rules that hold across both row types:

- **Answers are words, not checkboxes.** `YES` / `NO` / `UNKNOWN`, and `n/a` where a sub-question does not arise — Q1 B and C when Q1 A is No, or Q4.2 C when the transmission route is known. `n/a` is not `NO`, which would assert a finding the walk never made, and not `UNKNOWN`, which would claim the answer is unavailable when it was simply not asked. Put the one-clause reason in the rationale cell: `Not applicable — A = No.`
- **A question with no sub-questions gets a domain row and nothing else.** Question 4.1 is coded directly and has no letters, so it never gets sub-rows.
- **Keep every domain row, including ones the routing bypassed.** Give the bypassed row its answer cell as `—` and its rationale cell as `Not reached — Q2 = Yes routed to Q4.2`, and omit its sub-question rows entirely. The reviewer is comparing against a form with all seven questions; a missing domain row breaks the alignment, but empty sub-rows under a question that was never asked are just clutter.

**The citation rules do not relax because the cells are small.** Every specific fact, figure, or external claim carries a working hyperlink — to the signal's own source when restating signal-derived information, to a freshly verified source for anything external — per SKILL.md's citation-verification rule, including the scope-match and statistic-characterization tests. Brevity is a constraint on wording, not on evidence: if a claim will not fit with its source attached, shorten the claim rather than dropping the link. A figure that cannot be sourced within the cell does not belong in the cell.

**Domain 4 comparator rule still applies** (`domains_and_questions.md` §4b). The comparator goes in the **domain row**, not scattered through the sub-question rows, because it governs the overall answer: state the expected baseline, the observed figure, and the comparison between them, in the scoped population's units, each sourced. Where a baseline is unavailable the relevant sub-question is UNKNOWN — never YES with the gap noted alongside.

**Q4.2 B carries its tier** (`domains_and_questions.md` §4c). After the population name, the B row's rationale cell states the tier and measure — `Tier 1 (attack rate)` or `Tier 2 (doubling time)`. That measure's comparator sits with the others in the domain row, as above. UNKNOWN only when neither tier was available.

**Sub-question cells name their population** (`domains_and_questions.md` §4a). From Q2 onward, each sub-question rationale opens with the population it reasons about, in a few words. Where that is not the scoped population — including a subgroup within it — add the scoped-population coding in the same cell: `LTC residents (subgroup): YES. Scoped population: NO — …`. The Answer column carries the coding the rationale argues for; the second coding is what lets a reviewer see whether the population choice carried it.

**Domain 5 currency rule still applies** (`domains_and_questions.md` §5a). Date-stamp each capacity measure in its own sub-question row and mark it active or precedent: `2026 provincial vaccination plan, active` versus `2023 advisory, precedent only`.

## 5. Section 3 — Result

**Decision path.** Fill each blank with Y, N, or U. Write **–** for any question the routing did not reach, so the skipped questions are visibly skipped rather than ambiguously blank. Append the gate letter to the Q5.2 entry — `Q5.2c Y` — since the same answer at a different gate resolves to a different terminal, and the reviewer's comparison depends on knowing which gate was reached. This is the one addition to the form's printed layout, and it earns its place by making the terminal checkable.

Example, for a walk that went Q1 No → Q2 Yes → Q3 Yes → Q4.2 Yes → Q5.1 No → Q5.2c Yes:

> Q1 **N** → Q2 **Y** → Q3 **Y** → Q4.1 **–** / Q4.2 **Y** → Q5.1 **N** → Q5.2**c** **Y**

**Risk level.** Check exactly one. **Perform the mandatory four-step re-derivation in `domains_and_questions.md` §6a before checking this box** — arrival row, gate letter, answer, terminal read off the table. The re-derivation is performed once for the run; if a Recording Form was produced in the same turn, the box checked here and the level in that form's Part A Derivation line are the same lookup and must agree. Two artifacts disagreeing about the terminal is precisely the defect §6a exists to catch, and it is more visible, not less, when the reviewer has both in hand.

The sanity floor applies as always: a walk that reached Q5.1 cannot terminate below Moderate, and Very low is reachable only via Q4.1 = No or gate 5.2a = Yes.

**Confidence.** Check one level per Table 1 (`algorithm_essentials.md` §5), then list the main information gaps after the label — brief phrases, not the full confidence narrative. The directional analysis §5a requires ("coding B against the human baseline instead gives Q4.2 = N → gate 5.2b → Low") is too long for this cell; it belongs in the Recording Form. Since this is normally the only artifact produced, add the directional statement as a short note inside the confidence cell beneath the gaps, or beneath the terminal lookup line if it runs long.

**Terminal lookup line.** Reproduce verbatim, unaltered, including the closing sentence about Unknown following the Yes branch. It is the reviewer's own reference while they complete their independent walk. Do not correct, reformat, extend, or annotate it — not to add gate letters, not to align its wording with `domains_and_questions.md` §6.

## 6. Section 4 — Proposed actions

**Proposed actions get their own numbered section. They are not folded into other considerations.** Both assessors in the expert review reported that they could not readily find the actions when these were embedded in a general considerations block, and both marked format down for it. Actions are the part of a QIRA output an analyst acts on; they are the last thing that should require hunting for.

Three fields:

- **Source of actions.** QIRA expects each jurisdiction to predefine immediate actions per risk level (`risk_classification_and_actions.md` §2). Where the analyst has supplied that list, draw from it and say so. Where none exists, say so plainly — "no predefined list supplied for this jurisdiction; drawn from the QIRA manual's illustrative menu" — and note that a jurisdiction-specific list should be formalised. Never present menu items as though they were the jurisdiction's own standing actions.
- **Actions.** One per line, each beginning with a verb, each proportionate to the terminal risk level. At Very low or Low, "continue routine surveillance" and "no escalation warranted" are complete and correct answers; padding the list to look substantial misrepresents the finding. Scope each action to the window and territory actually assessed rather than issuing generic advice.
- **Reassessment trigger.** What would invalidate this assessment before the window closes — a count exceeding a stated threshold, publication of data that would settle an Unknown, a case in a previously unaffected area, expiry of the window itself.

Cross-cutting footnote items (IHR notification, cross-border sharing, political sensitivity) belong in section 5, not here, even though they may imply action. Section 4 is what this jurisdiction does about this event; section 5 is what a reader needs to know to interpret the assessment.

## 7. Section 5 — Other considerations

Everything that qualifies the reading of the assessment without being an action: the IHR Annex 2 determination and its four-criteria reasoning, the remaining cross-cutting footnotes from `risk_classification_and_actions.md` §3, the equity distribution concealed by a scoped average, any discrepancy between the signal and its underlying source, and any importation or spillover assumption with the question wording it changed.

Keep each to a short labelled paragraph. If a row does not apply, omit it rather than writing "none" — except the IHR Annex 2 row, which is always reported, including when no criteria are met, because a reader needs to see that the determination was made rather than skipped.

## 8. Questions the routing bypassed

The Recording Form drops questions the routing bypassed. **This document keeps a domain row for every one of the seven**, because the reviewer is comparing against a form that has all seven and a missing row breaks the alignment.

Give a bypassed question `—` in the Answer column and `Not reached — [reason]` in the rationale column, the reason being one short clause naming the routing decision responsible: `Not reached — Q2 = Yes routed to Q4.2`, or `Not reached — Q1 = Yes, skipped to gate 5.2e`. Omit its sub-question rows.

A bypassed question is not a question answered UNKNOWN, and the distinction carries real weight for a reviewer scoring aggregation and routing. Never write UNKNOWN as a way of filling a question that was never asked.

## 9. The aggregation notes in the domain rows

The italic notes in each domain row state mechanical rules. Five of the seven restate the manual directly (Q1, Q2, Q4.1, Q4.2, Q5.1). **Two are the form author's formalization of questions the manual leaves to judgement**: Q3's *"Yes iff any of A, B, C yes"* and Q5.2's *"Yes iff B, C, D all yes AND E no."* The QIRA manual states neither rule; it supplies guiding questions for both and, in Q5.2's case, explicitly calls for expert judgement on E.

Reproduce both notes verbatim — they are part of the form the reviewer is using, and they belong in the domain row where the main answer they govern sits. But **code Q3 and Q5.2 by the same judgement this skill applies everywhere else**, not by mechanical conjunction. Where the mechanical rule would give a different main answer than the coded one, say so explicitly in the domain row's rationale cell, beneath the rule:

> **Diverges from stated rule:** C = UNKNOWN alone, but B and D active and E immaterial → Main = YES

This is a substantive disagreement between two artifacts a reviewer is holding at once, and flagging it in the domain row is what lets them adjudicate it rather than read it as a coding error. It is also worth surfacing at the Step 12 confirmation pause as a **`CONFIRM:`** item the first time it arises for a given analyst — the resolution may be that their form should be amended, which is not this skill's call to make silently.

Note also that Q5.2's E is inverted in polarity: E asks whether major barriers exist, so **E = No supports capacities = Yes**. Getting this backwards flips the terminal by a full level.

## 10. Relationship to the Results Recording Form

**The Evaluation Form is a standalone deliverable — Part 1 filled, Part 2 blank — and does not carry the Recording Form with it.** When the analyst asks for the Evaluation Form, produce that and only that.

The two are separate artifacts serving separate readers. The Recording Form is the assessment's own paper trail; the Evaluation Form is a reviewer instrument. A reviewer running the full protocol will want both, since Part 2 directs them to read the skill's output in full and several component ratings (rationale quality, proposed actions, other considerations) score material that lives only in the Recording Form. But that is the analyst's call about what to circulate, not a reason to bundle. Mention once that those ratings need the Recording Form alongside, and leave it there.

**Reformatting an existing Recording Form is a normal way this format is requested.** The analyst may hand over a completed Recording Form — from an earlier run, another session, or another model — and ask for the Evaluation Form from it. When they do, do not re-run the walk. Transcribe: the codings, the terminal, the confidence, and the assumption are the source document's, and changing any of them silently would make the two documents disagree about the same assessment. Three points of care:

- **Convert the sub-question labels.** A Recording Form written against the WHO manual's global lettering (A4, B4, C4, D4, A5, B5–E5) needs converting to this skill's per-question lettering via the crosswalk in `domains_and_questions.md` §0. Q4.2 is where this bites: the manual's A4/B4/C4/D4 become A1/A2/B/C.
- **Compress, don't summarise away.** Recording Form rationale cells run to paragraphs; evidence cells here run to fragments. Keep every hyperlink and every comparator figure; drop the connective prose.
- **Check the source's Main answers against the form's stated rules** (§7). A Recording Form that predates the Evaluation Form's aggregation rules may contain a Main answer the rules would not produce. Flag the divergence in the evidence cell rather than adjusting the answer.

Where both artifacts do go out together, everything appearing in both must agree: assessment reference, scope statement, assumption, every sub-question coding, the terminal, and the confidence level. They are two renderings of one walk, not two walks.
