# QIRA — Results Recording Form Template

**Companion to**: `qira-assessor` SKILL.md. Read at Step 13 (populate output) and use as the literal output structure.

**Source**: *QIRA User Manual*, Annex 1. Jurisdictions may adapt this form to local needs — the fields below are the WHO-suggested default; note any deviation the analyst's context requires.

**The fillable structure itself lives in `assets/recording_form_blank.md`** — copy that file's structure directly into the output for each run. This file provides the field-by-field guidance for populating it correctly.

---

## Metadata block: field guidance

- **Assessment reference:** a locally-generated, human-readable label, not a real backend session ID (no tool exposes one) — format `QIRA-{jurisdiction code}-{YYYY-MM-DD}-{short hazard slug}-v{version}`, e.g. `QIRA-CA-2026-07-28-SALMONELLA-v2`. This is a labeling convention for the analyst's own tracking and for surfacing this run again later via content search — say so plainly if asked, rather than implying it's an official identifier.
- **Model:** state whichever model is actually active for this run (read this from the current session context each time — never hardcode a specific model name in this template, since the analyst can switch models between runs).
- **Date of QIRA / Version:** as before — version increments on each reassessment of the same signal.

## Original signal: field guidance

Reproduce the analyst's original signal text verbatim in the fenced code block, unedited — this is what makes the assessment fully auditable and reproducible from the document alone, independent of anything said in surrounding conversation. If the signal was given across multiple messages or refined partway through, use the final, complete version of the signal as it was actually assessed.

## Part A — Summary form: field guidance

- **Signal/event:**
- **Member State / subnational area:**
- **Brief summary of signal or event and scope of assessment:** time, place, person; what the event is and why it's of interest; geographical area and population in scope; forward-looking window (valid until when, absent major change). **The population stated here is the unit of assessment for every "case" count in the walk** (`domains_and_questions.md` §4a) — state it unambiguously, because a reader checking the Part B answers will check them against this line.
- **Risk level classification:** [Very low | Low | Moderate | High | Very high]
- **Derivation:** a single line showing the terminal was read off the routing table, in the form `arrival row → gate → answer → terminal` (e.g. "reached via Q5.1 = No → gate 5.2c → Yes → **Moderate**"). This is mandatory and must match the level stated above and every terminal named anywhere in Part B. See `domains_and_questions.md` §6a — a reviewed run has already reported a terminal that contradicted its own correctly-labelled gate, and this line is the control against that.
- **Rationale:** the specific findings that drove the routing outcome — name the domains and sub-questions that determined the path, not a generic restatement of the risk level.
- **Confidence level:** [Low | Moderate | High] with the specific information gaps or expert-agreement basis (Table 1 in `algorithm_essentials.md` §5). Per §5a, also state **which way** the assessment would move under the plausible alternative codings — naming the sub-question, the alternative answer, and the terminal it produces — and flag explicitly when the open calls all lean the same direction.
- **Proposed actions:** drawn from the Member State's predefined list where one exists (see `risk_classification_and_actions.md` §2); note explicitly if none exists and a generic menu was used instead.
- **Other considerations:** any footnote-level items from `risk_classification_and_actions.md` §3 that apply (IHR notification flag, cross-border sharing, political sensitivity, novel-hazard judgement call), and any assumptions made per `domains_and_questions.md` §7 (importation/spillover assumption, modified question wording).

## Part B — Question-by-question response form: field guidance

**Standing format**: `Domain | Overall Question | Answer | Rationale`. One row per domain/question actually reached — skip rows the routing logic bypassed entirely (e.g., Question 4.1's row when Domain 2 routed to Question 4.2 instead). The Domain column always carries the full domain name (not just a number), and the Overall Question column always carries the actual question text (not a paraphrase or placeholder).

**Fold the sub-question detail into the Rationale, don't give it separate rows.** Name and describe the specific sub-questions (A2, B2, C2, etc.) that significantly influenced the Overall answer, written out with enough content that a reader doesn't need to cross-reference the manual to know what "B2" means — e.g. "further exposure is likely (B2) because the product remains in circulation via an untraceable supply chain," not just "B2 = Yes."

**Citation scope is broader than "external facts only."** Every specific fact, statistic, or claim in a Rationale cell needs a traceable source:
- If it's a figure or fact drawn from the signal itself, cite back to the *signal's own source* (whatever was in its "Sources" field, verified at Step 3) — don't leave it uncited just because it technically came from the analyst's input, since the point is a fully traceable chain of evidence, not a distinction between "signal" and "external."
- If it's genuinely external (a comparative case, a historical precedent, a transmission characteristic, a clinical-management fact, a published statistic not in the signal), search and verify it, then hyperlink it the same way.
- The only things that don't need a citation are routing statements (e.g., "→ Domain 2") and restatements of the QIRA algorithm's own logic, which is already sourced via the reference files.
- If verification isn't feasible, say so plainly rather than presenting an unverified claim as sourced.

**Three further tests on every cited claim** (all added after expert review; see SKILL.md's citation section for the failures that prompted them):

- **Scope match.** The link must support the whole scope of the sentence it's attached to — all the jurisdictions, all the years. If the sourcing is narrower, narrow the sentence.
- **Correct characterization of statistics.** Name the measure (attack rate, incidence, risk ratio, CFR), its denominator, and its comparison group. Never restate a ratio as a rate, and never present a comparison across differently-constructed denominators as a single measure. If these can't be pinned down, paraphrase qualitatively instead of quoting a number.
- **Currency of capacity evidence.** In B5/C5/D5 rationale, date-stamp each measure cited and label it **active capacity** (in effect for this event, in this window) or **precedent** (a prior-event protocol with no evidence it's currently in force). Precedent alone does not carry a capacity sub-question to Yes — see `domains_and_questions.md` §5a.

**Comparator statements in Domain 4 rows.** Any Rationale cell answering Question 4.1 or the A4/C4/D4 sub-questions states the expected baseline, the observed figure, and the comparison between them, in the scoped population's units, each sourced (`domains_and_questions.md` §4b). Where a baseline is unavailable, the cell says so and the sub-question is coded Unknown — never asserted as Yes with the gap noted alongside.

Sub-question reference, domain by domain:

| Domain | Sub-questions | Overall question | Routing after Overall |
|---|---|---|---|
| 1. High-threat hazard | A1, B1, C1 | Does the signal/event involve a hazard predefined as a high threat in your geographical area? | If yes (no override) → **5.2e**. If no/unknown, or yes-with-override → Domain 2. |
| 2. Exposure | A2, B2, C2 | Is further exposure likely to take place? | If yes/unknown → Domain 3. If no → 4.1. |
| 3. Severity | A3, B3, C3 | Is the disease likely to be moderate to severe among cases in this population? | → 4.2 (severity answer determines which 4.2 branch, and later which 5.2 gate, is reached — see `domains_and_questions.md` §6). |
| 4.1 Spread and scale | (single question, no sub-letters — coded directly) | Are a significant number of people currently affected? | If no → terminal (Very low). If yes/unknown → **5.2a**. |
| 4.2 Spread and scale | A4, B4, C4, D4 | Could a high number of cases or substantial geographical spread be expected in future? | Via Q3=No: if no → **5.2a**, if yes/unknown → **5.2b**. Via Q3=Yes/Unknown: if no → **5.2b**, if yes/unknown → 5.1. |
| 5.1 Capacity | A5 | Is the health care system likely to be overwhelmed? | If no → **5.2c**. If yes/unknown → **5.2d**. |
| 5.2 Capacity | B5, C5, D5, E5 | Are capacities for prevention and control measures in place? | Terminal — resolves risk level per `domains_and_questions.md` §6. **Always carry the specific gate label (5.2a/b/c/d/e) in the Domain column** — which gate you're at changes the terminal mapping. |

## Compatibility note

This is a working paper-trail document, not a formatted deliverable by default — render it as a clean markdown table/summary unless the analyst asks for a specific downstream format (e.g., inserting into a Word template or a specific bulletin field).
