---
name: qira-assessor
description: Walk any acute public health signal or event through the WHO Quick and Immediate Risk Assessment (QIRA) algorithm — a fast, hierarchical yes/no/unknown decision tree across five domains (high-threat hazard, exposure, severity, spread/scale, capacity) that resolves to a risk level (very low to very high) plus predefined immediate actions. Use this whenever the user provides a public health signal, outbreak report, or event description and asks for a QIRA assessment, a "quick risk assessment", or an immediate risk triage. Also use for questions about how QIRA routes a given answer, what risk level an event resolves to, or how to document a QIRA run in the Results Recording Form. Supports autonomous, hybrid, and interactive walkthrough modes.
compatibility: Portable — pure Markdown reasoning skill, no external tools, scripts, or MCP dependencies required. The decision-tree diagram in assets/qira_decision_tree.md renders wherever Mermaid is supported (GitHub, Obsidian, most Markdown viewers); it degrades gracefully to a plain code block elsewhere.
metadata:
  author: Adan
  version: 1.0.0
  tested: 4-signal battery (Salmonella/Canada, Ebola-Bundibugyo/importation-to-Canada, H5N1/Cambodia, measles/Bangladesh), 2026-07-10 — see references/domains_and_questions.md changelog note
---

# QIRA Assessor

A general-purpose skill for applying the WHO Quick and Immediate Risk Assessment (QIRA) algorithm to any acute public health signal or event. QIRA is a fast, hierarchical decision tree: each domain's answer determines which question comes next, and the walk terminates at one of five risk levels with no separate scoring or averaging step.

This skill is deliberately not scoped to any single program or bulletin — it applies to any jurisdiction or context the user specifies. If the user wants a program-specific adaptation (like a standing scope note for a recurring event or bulletin), that belongs in a separate companion reference file layered on top of this skill, not baked into it.

## Reading order

1. `references/algorithm_essentials.md` — what QIRA is, scope-setting, confidence levels, limitations (read this first, always).
2. `references/domains_and_questions.md` — the five domains and the full routing logic (read before Steps 4–8 below).
3. `references/risk_classification_and_actions.md` — risk levels, predefined immediate actions, cross-cutting footnotes (read before Steps 9–11).
4. `references/recording_form_template.md` — field-by-field guidance for the output template (read before Step 13).
5. `references/worked_example.md` — a condensed worked example for calibrating depth and voice (read once, or whenever a fresh example would help).
6. `assets/recording_form_blank.md` — the actual fillable Recording Form structure; copy this into the output at Step 13.
7. `assets/qira_decision_tree.md` — a Mermaid visual of the full routing logic; render or embed this when a visual aid would help an analyst follow or explain a walk (e.g., a novel or contested path), or when the output itself calls for a diagram.

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

## Step 8 — Domain 5: Capacity

Apply §5. This is where the walk terminates. Use the **consolidated routing table** in `domains_and_questions.md` §6 to determine the final risk level — track which path led to Question 5.2 (there are several), since the same Yes/No answer to 5.2 maps to different risk levels depending on the path.

## Step 9 — Confirm risk level

State the terminal risk level and the exact path taken (which domains were walked, which were skipped and why). This is the point at which hybrid-mode analysts should see the full reasoning if they haven't already. If the path was unusual, contested, or would benefit from a visual (a novel hazard, a Domain 1 override decision, or a request to explain the algorithm itself), render or point to `assets/qira_decision_tree.md` alongside the text explanation rather than as a substitute for it.

## Step 10 — Confidence level

Apply Table 1 from `algorithm_essentials.md` §5. Name the specific information gaps or areas of expert agreement/disagreement driving the confidence rating — don't just assert a level.

## Step 11 — Immediate actions and escalation flag

Select actions per `risk_classification_and_actions.md` §2 — use the analyst's own predefined list if one exists; otherwise use the illustrative menu and flag that a jurisdiction-specific list should be formalized. Apply the cross-cutting footnotes from §3 (IHR Annex 2 check, cross-border sharing, political sensitivity, novel-hazard override) regardless of risk level.

## Step 12 — Confirmation pause (hybrid/interactive only)

Present the full routing path, risk level, confidence level, and any judgement calls or assumptions for analyst sign-off before finalizing output. In interactive mode this has already happened incrementally at each domain; treat Step 12 as a final consolidated check rather than a fresh one.

## Step 13 — Populate the Results Recording Form

Copy the structure from `assets/recording_form_blank.md` and fill it in, using `references/recording_form_template.md` for field-by-field guidance. Only populate Part B rows for questions actually asked; note skipped questions and why. When labeling the Question 5.2 row, always include the specific gate (5.2a/b/c/d/e) — see `references/domains_and_questions.md` §6.

## Step 14 — Present output

Deliver the completed Recording Form. If the walk relied on an importation/spillover assumption, surface that prominently rather than burying it in the "Other considerations" field — it changes how the whole assessment should be read.
