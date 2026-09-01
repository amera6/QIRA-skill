---
name: qira-assessor
description: Walk any acute public health signal or event through the WHO Quick and Immediate Risk Assessment (QIRA) algorithm — a fast, hierarchical yes/no/unknown decision tree across five domains (high-threat hazard, exposure, severity, spread/scale, capacity) that resolves to a risk level (very low to very high) plus predefined immediate actions. Use this whenever the user provides a public health signal, outbreak report, or event description and asks for a QIRA assessment, a "quick risk assessment", or an immediate risk triage. Also use for questions about how QIRA routes a given answer, what risk level an event resolves to, or how to document a QIRA run in the Results Recording Form. Supports autonomous, hybrid, and interactive walkthrough modes.
compatibility: Core skill is portable — pure Markdown reasoning, no dependencies required for running assessments. assets/qira_decision_tree.md renders wherever Mermaid is supported, degrading to a plain code block elsewhere. One optional component, scripts/extract_docx_comments.py, requires a Python 3 environment with filesystem access — only needed for the Step 16 comment-extraction workflow, not for core assessment.
metadata:
  author: Adan
  version: 1.3.0
  tested: 4-signal battery (Salmonella/Canada, Ebola-Bundibugyo/importation-to-Canada, H5N1/Cambodia, measles/Bangladesh), 2026-07-10 — see references/domains_and_questions.md changelog note
  reviewed: 2-signal expert review (raccoon rabies/Quebec, iGAS/Quebec) by two PHAC risk assessors, 2026-08-19/20 — 18 comments; v1.3.0 addresses terminal mis-derivation, population-unit drift, evidence currency, statistic characterization, claim-scope overreach, and unstated comparators
---

# QIRA Assessor

A general-purpose skill for applying the WHO Quick and Immediate Risk Assessment (QIRA) algorithm to any acute public health signal or event. QIRA is a fast, hierarchical decision tree: each domain's answer determines which question comes next, and the walk terminates at one of five risk levels with no separate scoring or averaging step.

This skill is deliberately not scoped to any single program or bulletin — it applies to any jurisdiction or context the user specifies. If the user wants a program-specific adaptation (like a standing scope note for a recurring event or bulletin), that belongs in a separate companion reference file layered on top of this skill, not baked into it.

## Critical: two different kinds of "interpretation" — do not conflate them

**When explaining the algorithm itself** — why it's structured the way it is, why a design choice makes sense, what a routing pattern "represents" conceptually — stick strictly to what's explicitly stated in the source manual and its reference files here. Do not volunteer narrative rationale for the algorithm's own design unless the analyst specifically asks for it, and even then, explicitly flag it as your own synthesis rather than the manual's stated reasoning. If asked "why does the algorithm do X," check whether the manual actually says why before answering — most of the time it just states the rule, not the rationale, and that absence should be stated plainly rather than filled in.

**When answering the algorithm's own questions for a specific signal** — coding A2, B3, E5, and so on against the facts the analyst has provided — judgment and interpretation are expected and necessary. This is what running a risk assessment *is*: the manual itself repeatedly calls for "expert judgement" (e.g., Question 5.2.E on vulnerabilities/barriers) and provides no numeric thresholds for several questions (e.g., Question 4.1's "significant number of people affected"). Reason openly about how signal-specific facts map onto each question, and show that reasoning — this is substantiated interpretation *of the evidence*, not invented interpretation *of the algorithm's design*, and it's the core value this skill provides.

## Critical: external evidence in rationale must be verified and hyperlinked

When a sub-question's rationale draws on something beyond the signal itself and the QIRA reference files — a comparative case, a historical precedent, a published statistic, a transmission characteristic of a pathogen — that claim needs an actual verified source, not a recollection presented as fact. This applies whether the mode is Autonomous, Hybrid, or Interactive.

- **Search before citing.** Use web search to find a real, current source for the specific claim before including it. Do not write out a plausible-sounding citation (a study, a case, a statistic) from memory and present it as sourced — that is exactly the failure mode this rule exists to prevent, and it has happened in this skill's own worked examples before this rule was added.
- **Hyperlink the claim itself**, using standard Markdown link syntax (`[precedent description](https://...)`), pointing to the specific verified source — not a generic search-engine link or a homepage. Prefer primary or authoritative sources (CDC, WHO, PHAC, peer-reviewed literature, major wire services) over aggregators or forums, consistent with normal sourcing practice. In the Results Recording Form specifically, these hyperlinks belong in the Rationale column of the Part B table (see Step 13) — not off to the side or only in prose.
- **If verification isn't feasible in the moment** (no search available, or nothing adequate found), say so plainly — state the claim as an unverified recollection and flag it for the analyst's own verification, rather than presenting it with false confidence.
- **Cite every specific fact or claim, not just genuinely external ones.** A claim like "imported cases into non-endemic health systems have historically remained isolated" is external empirical evidence and needs a freshly verified, hyperlinked source. A claim like "the signal reports 189 cases" is restating the analyst's own input and doesn't need a *new* search — but when that figure appears in a Rationale cell of the Recording Form, cite it back to the signal's own source (from its "Sources" field, verified at Step 3) rather than leaving it uncited. The goal is a fully traceable chain of evidence, not a distinction between "signal" and "external." The only things that don't need a citation are routing statements and restatements of the QIRA algorithm's own logic.
- **This adds tool calls and time.** Searching and verifying every external claim is slower than reasoning from recall. That tradeoff is deliberate — an unverifiable citation in a real risk assessment is worse than a visibly-flagged gap.

**Verification means more than "the source exists."** A link that resolves is necessary and not sufficient. Two further tests, both of which have failed in reviewed runs:

- **The link must support the full scope of the sentence it is attached to.** A claim spanning several jurisdictions and several years needs sources covering those jurisdictions and years — one regional dataset ending three years ago does not support it. If the available sourcing is narrower than the claim, narrow the claim to match rather than letting the link imply coverage it doesn't have. A reviewer caught exactly this: a multi-country, multi-year trend statement hyperlinked to a single-city dataset that stopped in 2023.
- **Quantitative claims must be characterized correctly.** Before citing a statistic, state what measure it actually is (attack rate, incidence, risk ratio, odds ratio, CFR), over what denominator, and against what comparison group. Do not restate a ratio as a rate, and do not present a comparison between two differently-constructed denominators as though it were a single measure. A reviewer flagged a "1,940-fold the background attack rate" claim on both counts — the figure was a risk ratio, and it compared a household attack rate against community background incidence, which are different measures. **If the measure or its denominators can't be pinned down from the source, paraphrase the finding qualitatively ("close contacts face substantially elevated risk") instead of quoting a number.** A misdescribed statistic is worse than no statistic, because it looks precise.

## Reading order

1. `references/algorithm_essentials.md` — what QIRA is, scope-setting, confidence levels, limitations (read this first, always).
2. `references/domains_and_questions.md` — the five domains and the full routing logic (read before Steps 4–8 below).
3. `references/risk_classification_and_actions.md` — risk levels, predefined immediate actions, cross-cutting footnotes (read before Steps 9–11).
4. `references/ihr_annex2_decision_instrument.md` — the actual IHR Annex 2 four-criteria decision instrument and always-notifiable disease list, read at Step 11 instead of relying on background knowledge for the footnote (i) check.
5. `references/recording_form_template.md` — field-by-field guidance for the output template (read before Step 13).
6. `references/worked_example.md` — a condensed worked example for calibrating depth and voice (read once, or whenever a fresh example would help).
7. `assets/recording_form_blank.md` — the actual fillable Recording Form structure; copy this into the output at Step 13.
8. `assets/qira_decision_tree.md` — a Mermaid visual of the full routing logic; render or embed this when a visual aid would help an analyst follow or explain a walk (e.g., a novel or contested path), or when the output itself calls for a diagram.
9. `scripts/extract_docx_comments.py` — used at Step 16 only, when extracting reviewer comments from an annotated Word document. Not needed for a standard assessment run.

---

## Step 1 — Confirm mode

Three modes:

- **Autonomous** — complete the full walk and produce the final Recording Form without pausing. Best for batch processing or when the analyst has already reviewed similar signals.
- **Hybrid (default)** — walk the domains silently, then pause once before final output to present the full routing path, risk level, and any judgement calls (Domain 1 override, novel-hazard classification, assumption use) for analyst confirmation or correction.
- **Interactive** — pause after each domain (or each judgement call) so the analyst can see the reasoning and confirm, correct, or override before continuing. Best for training, novel hazards, or high-stakes signals.

If the user doesn't specify, default to Hybrid and say so.

## Step 2 — Read references

Load the five reference files above. For a first-time run in a session, read all five; for a subsequent run in the same conversation, a quick re-check of `domains_and_questions.md` §6 (the consolidated routing table) is usually sufficient, since that's the part most prone to being misremembered.

## Step 3 — Parse the signal and define scope

Extract or ask for: the event/signal description, the affected geographical area, the population of concern, and the date/recency of the information. Per `algorithm_essentials.md` §3, explicitly state:

- What is the event of interest?
- Why is it of interest?
- Which geographical area is affected?
- Who is or may be affected?
- What is the forward-looking window for this assessment?

**Preserve the analyst's original signal text verbatim** at this point — it goes unedited into the Recording Form's "Original signal" code block at Step 13, regardless of how it gets paraphrased or restructured for the walk itself.

**The population named here sets the unit of assessment for the entire walk.** By default, every "case," "number affected," and "attack rate" in every downstream question is counted in that population — see `domains_and_questions.md` §4a. Restate the population explicitly at Step 7 and check the Domain 3, 4, and 5 answers against it before finalizing.

If the analyst's signal makes a different population the more informative unit (a zoonotic hazard where the animal-side picture is what's actually moving), **raise it here, at scope-setting** — offer either a redefined scope or a second run alongside the first. An analyst may override the default and have the overall answers coded in other units; if they do, document it per §4a's override rules and report what the default coding would have produced. Do not raise the unit question for the first time mid-walk at Domain 4: by then it presents as a coding choice with a two-level swing attached, rather than the scope decision it actually is.

If the user hasn't supplied a predefined high-threat hazard list for their context, note that Domain 1 will default to NO/UNKNOWN unless they supply one (see `algorithm_essentials.md` §4).

**Importation/spillover check**: if the source event is outside the jurisdiction being assessed, or is a zoonotic pathogen not yet confirmed in humans, flag this immediately — per `algorithm_essentials.md` §6.2 and `domains_and_questions.md` §7, QIRA requires an explicit assumption (treat the event as already detected within the jurisdiction) before the tree can be walked at all. State the assumption plainly and get analyst sign-off on it in hybrid/interactive mode before proceeding — this is the single most consequential judgement call in the whole walk, since it determines what every downstream answer is actually conditioned on.

## Step 4 — Domain 1: High-threat hazard

Apply the Domain 1 logic from `domains_and_questions.md` §1. If it resolves YES, the walk skips straight to Question 5.2 — go directly to Step 8. Otherwise continue to Step 5.

## Step 5 — Domain 2: Exposure

Apply §2. Route to Domain 3 (Step 6) or divert to Question 4.1 (Step 7) per the outcome.

## Step 6 — Domain 3: Severity

Apply §3. Always proceeds to Question 4.2, but note which branch (Q3 answer) will be needed for the Domain 5 routing junction in Step 8.

## Step 7 — Domain 4: Potential spread and scale

Apply §4, using whichever of Question 4.1 or 4.2 applies given the path taken so far. Terminal "Very low" resolves here if Question 4.1 = NO — in that case, skip straight to Step 10 (there's no Domain 5 to walk).

Two mandatory checks before recording the overall answer, both from `domains_and_questions.md` §4a–4b:

1. **Restate the scoped population and confirm the overall answer is in its units.** Sub-questions may draw on animal, environmental, or other-population evidence; by default the overall answer counts cases in the Step 3 population only. This is the single most common way a walk goes wrong by two risk levels. If a unit override was elected at Step 3, apply it and record it per §4a.
2. **State the comparator** — expected baseline, observed figure, and the comparison between them, each sourced. No baseline available means the sub-question is Unknown; it does not mean answer Yes and note the gap.

## Step 8 — Domain 5: Capacity

Apply §5. This is where the walk terminates. Use the **consolidated routing table** in `domains_and_questions.md` §6 to determine the final risk level — track which path led to Question 5.2 (there are several), since the same Yes/No answer to 5.2 maps to different risk levels depending on the path.

## Step 9 — Derive and confirm the risk level

**Perform the mandatory four-step re-derivation in `domains_and_questions.md` §6a before writing the terminal level anywhere.** State, in writing and as separate steps: the arrival row, the gate letter, the answer at that gate, and the terminal read off the table for that gate-and-answer pair. This is a lookup performed at this moment, not a confirmation of a level formed earlier in the walk. A live run has already reported Low from a gate that maps to Moderate, with the gate correctly labelled — so treat this derivation as a hard control, not a formality.

Then apply the sanity floor: a walk that reached Question 5.1 cannot terminate below Moderate, and Very low is reachable only via Q4.1 = No or gate 5.2a = Yes. A violation means a derivation error, not a surprising finding.

If the derived level conflicts with your analytical read of the event, **do not adjust the terminal** — locate the upstream sub-question responsible, fix its coding if it is genuinely wrong, and re-derive. If the coding is right and the level still feels wrong, that tension is reportable content for the confidence section (Step 10), not grounds for overriding the table.

Finally, state the exact path taken (which domains were walked, which were skipped and why). This is the point at which hybrid-mode analysts should see the full reasoning if they haven't already. If the path was unusual, contested, or would benefit from a visual (a novel hazard, a Domain 1 override decision, or a request to explain the algorithm itself), render or point to `assets/qira_decision_tree.md` alongside the text explanation rather than as a substitute for it.

## Step 10 — Confidence level

Apply Table 1 from `algorithm_essentials.md` §5. Name the specific information gaps or areas of expert agreement/disagreement driving the confidence rating — don't just assert a level.

**State the direction of error, not just its size.** For each judgement call that could reasonably have gone the other way, say which way the alternative coding would move the terminal level and by how much (see `algorithm_essentials.md` §5a). "A different analyst could land elsewhere" is not usable by a reviewer; "coding C4 against the human baseline instead would give 4.2 = No → gate 5.2b → Low" is. Where several open calls all push the same direction, say so explicitly — that is a systematic lean in the assessment, and it is the most useful thing a confidence statement can tell a reviewer.

## Step 11 — Immediate actions and escalation flag

Select actions per `risk_classification_and_actions.md` §2 — use the analyst's own predefined list if one exists; otherwise use the illustrative menu and flag that a jurisdiction-specific list should be formalized. Apply the cross-cutting footnotes from §3. For footnote (i) — the IHR Annex 2 check — consult `references/ihr_annex2_decision_instrument.md` directly rather than relying on background knowledge: confirm whether the hazard is one of the four always-notifiable diseases, and if not, run the four-criteria assessment and report the result explicitly, independent of the QIRA risk level.

## Step 12 — Confirmation pause (hybrid/interactive only)

Chat messages don't support functional jump-to-anchor links, so don't rely on markdown links (`[text](#anchor)`) to help the analyst navigate back to a specific item — they won't actually scroll-jump in this interface. Instead, use this two-part convention to make judgement calls easy to find and respond to:

1. **Flag inline, at the point it occurs.** Whenever the walk includes an assumption (importation/spillover, §7 of `domains_and_questions.md`), a Domain 1 override (C1), a genuinely uncertain sub-question coding, or a novel/contested classification, tag it right there with a consistent text marker — **`CONFIRM:`** — followed by a short, quotable phrase describing the specific call. No emoji or other decorative markers — plain bold text only.
2. **Consolidate into a numbered checklist before finalizing.** At the confirmation pause, list every flagged item as a numbered list, each one quoting the exact flagged phrase from step 1 in quotation marks (not just describing it generically). This lets the analyst reply with numbers ("2 and 4 look right, change 3 to X") instead of re-reading the full walk to find what needs a decision.

Example of the checklist format:

> **Please confirm or correct:**
> 1. Spillover assumption: *"assuming a human case has been identified"* — reasonable, or should this run as pure animal-only surveillance instead?
> 2. Domain 1 override (C1 = Yes): *"novel exposure pathway... full walk gives more actionable detail"* — agree, or prefer the standard skip to 5.2e?
> 3. Q3 severity coded Yes/Unknown: *"clade's human-severity profile isn't established"* — any additional data to firm this up?

In interactive mode, apply step 1 (inline flagging) at each domain as it's walked; step 2's consolidated list becomes a shorter final recap rather than a fresh one, since most items will have already been confirmed along the way.

## Step 13 — Populate the Results Recording Form

Copy the structure from `assets/recording_form_blank.md` and fill it in, using `references/recording_form_template.md` for field-by-field guidance. Populate the metadata block (Assessment reference, Model, Date, Version) and the Original signal code block first — the latter must be the analyst's verbatim text preserved from Step 3. Part B always uses the standing format `Domain | Overall Question | Answer | Rationale` — one row per domain/question actually reached, full domain name and full question text in their respective columns, with influential sub-questions named and described within the Rationale rather than broken into separate rows. When labeling the Question 5.2 row, always include the specific gate (5.2a/b/c/d/e) — see `references/domains_and_questions.md` §6. Every specific fact or claim in a Rationale cell gets a hyperlink — to the signal's own source if restating signal-derived information, or to a freshly verified source for anything external — per the citation-verification rule above.

## Step 14 — Present output

Deliver the completed Recording Form. If the walk relied on an importation/spillover assumption, surface that prominently rather than burying it in the "Other considerations" field — it changes how the whole assessment should be read.

## Step 15 — Export a standalone Markdown file (on request)

When the analyst wants the Recording Form as a file for external review (e.g., committing to a repo's `outputs/` folder for colleagues to read), create a standalone `.md` file containing exactly the chat output — metadata block, Original signal code block, Part A, Part B — with no additional commentary. Name it after the Assessment reference (e.g., `QIRA-QC-2026-07-29-LEGIONELLOSIS-v1.md`), so the filename alone identifies the run. This file is meant to be committed by the analyst using their own git tooling — this skill does not push to any repository itself, and should not be asked to handle git credentials or tokens.

## Step 16 — Extract reviewer comments from an annotated Word document (on request)

If a colleague has annotated an exported `.docx` version of a Recording Form (e.g., via Word or SharePoint) and the analyst brings the commented file back, use `scripts/extract_docx_comments.py` to pull every comment into Markdown:

```
python3 scripts/extract_docx_comments.py reviewed.docx -o comments.md
```

This extracts each comment's author, date, the exact text it's anchored to, the comment body, and threaded replies (nested under their parent) — no manual re-reading of the Word document required. The script has no third-party dependencies (stdlib `zipfile` + `xml.etree` only) and degrades gracefully to "no comments found" if the document has none. This is an on-demand step, not a live sync — it runs whenever the analyst supplies a commented file, not automatically when SharePoint comments are added.
