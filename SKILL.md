---
name: "qira-assessor"
description: Walk any acute public health signal or event through the WHO Quick and Immediate Risk Assessment (QIRA) algorithm — a fast, hierarchical yes/no/unknown decision tree across five domains (high-threat hazard, exposure, severity, spread/scale, capacity) that resolves to a risk level (very low to very high) plus predefined immediate actions. Use this whenever the user provides a public health signal, outbreak report, or event description and asks for a QIRA assessment, a "quick risk assessment", or an immediate risk triage. Also use for questions about how QIRA routes a given answer, what risk level an event resolves to, or how to document a QIRA run in the Results Recording Form. Supports autonomous, hybrid, and interactive modes, and two output formats — the standard Recording Form, and an "evaluation form" mirroring Part 1 of the QIRA Skill Evaluation document — use that whenever the analyst asks for an evaluation form, reviewer form, Part 1 mirror, or output for reviewer benchmarking.
compatibility: Core skill is portable — pure Markdown reasoning, no dependencies required for running assessments. assets/qira_decision_tree.md renders wherever Mermaid is supported, degrading to a plain code block elsewhere. One optional component, scripts/extract_docx_comments.py, requires a Python 3 environment with filesystem access — only needed for the Step 16 comment-extraction workflow, not for core assessment.
metadata:
  author: Adan
  version: 1.8.0
  tested: 4-signal battery (Salmonella/Canada, Ebola-Bundibugyo/importation-to-Canada, H5N1/Cambodia, measles/Bangladesh), 2026-07-10 — see references/domains_and_questions.md changelog note
  reviewed: 2-signal expert review (raccoon rabies/Quebec, iGAS/Quebec) by two PHAC risk assessors, 2026-08-19/20 — 18 comments; v1.3.0 addresses terminal mis-derivation, population-unit drift, evidence currency, statistic characterization, claim-scope overreach, and unstated comparators
  evaluated: 2-assessor expert evaluation (anaplasmosis/Quebec), 2026-09 — risk level concordant within one level (skill Low, both assessors Moderate, both judged defensible), no fabrication found; v1.6.0 adds a minimum-information scope gate at Step 3, a source hierarchy requiring authoritative sources for scientific claims, and proposed actions as their own Evaluation Form section
  reviewer_fixes: Clarence Tam (PHAC) review, 2026-09 — v1.7.0 applies fixes 4, 5 and 7 from that review's fix list (reviewer comments C6 and C7) — every sub-question names the population it reasons about, with a population consistency sweep before terminal derivation (Step 9, domains_and_questions.md §4a); a concentration check that raises the scope choice at Step 3 (Step 3b); and two-tier coding for Q4.2 B (domains_and_questions.md §4c). The remaining fixes on that list are not part of this release
  concordance: 2-assessor blinded comparison (West Nile virus/Ontario), 2026-09-22 — both PHAC assessors independently coded Q3 = No against an infection denominator and terminated at Very low; v1.7.0 coded Q3 = Yes from ascertained-case severity statistics and terminated at Low. v1.8.0 adds the Q3 denominator rule (domains_and_questions.md §3a) and Step 6's pre-coding check; re-running the same signal under v1.8.0 reproduces Very low, giving exact concordance with both assessors
  version_note: v1.8.0 changes walk behaviour at Domain 3 and can move a terminal by one level for any hazard with a large subclinical fraction; re-run open assessments made under v1.7.0 or earlier where Q3 was coded from reported-case statistics. v1.5.0 was reserved for these fixes before v1.6.0 shipped; they are layered onto the v1.6.0 file set instead and numbered v1.7.0 because fixes 4, 5 and 7 change walk behaviour. No v1.5.0 exists
---

# QIRA Assessor

A general-purpose skill for applying the WHO Quick and Immediate Risk Assessment (QIRA) algorithm to any acute public health signal or event. QIRA is a fast, hierarchical decision tree: each domain's answer determines which question comes next, and the walk terminates at one of five risk levels with no separate scoring or averaging step.

This skill is deliberately not scoped to any single program or bulletin — it applies to any jurisdiction or context the user specifies. If the user wants a program-specific adaptation (like a standing scope note for a recurring event or bulletin), that belongs in a separate companion reference file layered on top of this skill, not baked into it.

## Critical: two different kinds of "interpretation" — do not conflate them

**When explaining the algorithm itself** — why it's structured the way it is, why a design choice makes sense, what a routing pattern "represents" conceptually — stick strictly to what's explicitly stated in the source manual and its reference files here. Do not volunteer narrative rationale for the algorithm's own design unless the analyst specifically asks for it, and even then, explicitly flag it as your own synthesis rather than the manual's stated reasoning. If asked "why does the algorithm do X," check whether the manual actually says why before answering — most of the time it just states the rule, not the rationale, and that absence should be stated plainly rather than filled in.

**When answering the algorithm's own questions for a specific signal** — coding Q2 A, Q3 B, Q5.2 E, and so on against the facts the analyst has provided — judgment and interpretation are expected and necessary. This is what running a risk assessment *is*: the manual itself repeatedly calls for "expert judgement" (e.g., Question 5.2 E on vulnerabilities/barriers) and provides no numeric thresholds for several questions (e.g., Question 4.1's "significant number of people affected"). Reason openly about how signal-specific facts map onto each question, and show that reasoning — this is substantiated interpretation *of the evidence*, not invented interpretation *of the algorithm's design*, and it's the core value this skill provides.

## Critical: external evidence in rationale must be verified and hyperlinked

When a sub-question's rationale draws on something beyond the signal itself and the QIRA reference files — a comparative case, a historical precedent, a published statistic, a transmission characteristic of a pathogen — that claim needs an actual verified source, not a recollection presented as fact. This applies whether the mode is Autonomous, Hybrid, or Interactive.

- **Search before citing.** Use web search to find a real, current source for the specific claim before including it. Do not write out a plausible-sounding citation (a study, a case, a statistic) from memory and present it as sourced — that is exactly the failure mode this rule exists to prevent, and it has happened in this skill's own worked examples before this rule was added.
- **Hyperlink the claim itself**, using standard Markdown link syntax (`[precedent description](https://...)`), pointing to the specific verified source — not a generic search-engine link or a homepage. In the Results Recording Form specifically, these hyperlinks belong in the Rationale column of the Part B table (see Step 13) — not off to the side or only in prose.
- **If verification isn't feasible in the moment** (no search available, or nothing adequate found), say so plainly — state the claim as an unverified recollection and flag it for the analyst's own verification, rather than presenting it with false confidence.
- **Cite every specific fact or claim, not just genuinely external ones.** A claim like "imported cases into non-endemic health systems have historically remained isolated" is external empirical evidence and needs a freshly verified, hyperlinked source. A claim like "the signal reports 189 cases" is restating the analyst's own input and doesn't need a *new* search — but when that figure appears in a Rationale cell of the Recording Form, cite it back to the signal's own source (from its "Sources" field, verified at Step 3) rather than leaving it uncited. The goal is a fully traceable chain of evidence, not a distinction between "signal" and "external." The only things that don't need a citation are routing statements and restatements of the QIRA algorithm's own logic.
- **This adds tool calls and time.** Searching and verifying every external claim is slower than reasoning from recall. That tradeoff is deliberate — an unverifiable citation in a real risk assessment is worse than a visibly-flagged gap.

**Source hierarchy — scientific claims need scientific sources.**

Two different kinds of claim appear in a QIRA rationale, and they carry different sourcing standards:

- **Event facts** — what was reported, when, how many, by whom. A news report is a legitimate source for these, because the news report often *is* the signal. Cite it as reported and attribute it: "a media report of 21 August states 50 cases."
- **Scientific claims** — transmission characteristics, incubation and infectious periods, case fatality and hospitalisation proportions, incidence and baseline rates, vector biology and seasonality, clinical management and treatment efficacy, immunity and vaccine performance, geographical distribution. **These require an authoritative source, and a news article is not one**, however reputable the outlet.

Preference order for a scientific claim, highest first:

1. Peer-reviewed literature, and systematic reviews or guidelines built on it.
2. National and international public health agencies and their surveillance outputs — WHO, PAHO, ECDC, CDC, PHAC, national and provincial institutes (INSPQ, Santé publique France, UKHSA), including their published surveillance reports, epidemiological bulletins and technical guidance.
3. Government clinical or laboratory guidance, and professional or clinical society guidelines.
4. Major wire services and established outlets — **for event facts only**, or as a pointer to the authoritative source underneath.
5. Aggregators, secondary summaries, forums, commercial sites — not used.

Two rules follow:

- **Never let a news article carry a scientific claim alone.** If a news piece quotes an agency or a study, that quotation is a pointer, not the source: go to the agency page or the paper and cite that. Citing an outlet quoting an institute, when the institute publishes the same fact directly, is a sourcing failure a reviewer will catch — and did. If the authoritative source genuinely cannot be located, keep the news citation, label it explicitly as a secondary report of the underlying claim, and flag it for verification.
- **Prefer the most recent authoritative release, and say which year the data cover.** Where a signal spans several years, a comparator built on the earliest of them will be challenged. Check whether a more recent surveillance report exists before settling on an older one, and state the period each cited figure describes. A reviewer scored an otherwise sound assessment down specifically because its comparator rested on the earliest year in the signal's range while later data existed.

**Verification means more than "the source exists."** A link that resolves is necessary and not sufficient. Two further tests, both of which have failed in reviewed runs:

- **The link must support the full scope of the sentence it is attached to.** A claim spanning several jurisdictions and several years needs sources covering those jurisdictions and years — one regional dataset ending three years ago does not support it. If the available sourcing is narrower than the claim, narrow the claim to match rather than letting the link imply coverage it doesn't have. A reviewer caught exactly this: a multi-country, multi-year trend statement hyperlinked to a single-city dataset that stopped in 2023.
- **Quantitative claims must be characterized correctly.** Before citing a statistic, state what measure it actually is (attack rate, incidence, risk ratio, odds ratio, CFR), over what denominator, and against what comparison group. Do not restate a ratio as a rate, and do not present a comparison between two differently-constructed denominators as though it were a single measure. A reviewer flagged a "1,940-fold the background attack rate" claim on both counts — the figure was a risk ratio, and it compared a household attack rate against community background incidence, which are different measures. **If the measure or its denominators can't be pinned down from the source, paraphrase the finding qualitatively ("close contacts face substantially elevated risk") instead of quoting a number.** A misdescribed statistic is worse than no statistic, because it looks precise. **The commonest instance of this inside QIRA is Domain 3's denominator**: a case fatality rate computed within a severe subset — neuroinvasive disease, ICU admissions, hospitalised cases — is not the fatality proportion of the event, and carrying it into Q3 A as though it were inflates severity by roughly the inverse of the ascertainment fraction. See `domains_and_questions.md` §3a.

## Reading order

1. `references/algorithm_essentials.md` — what QIRA is, scope-setting, confidence levels, limitations (read this first, always).
2. `references/domains_and_questions.md` — the five domains and the full routing logic (read before Steps 4–8 below).
3. `references/risk_classification_and_actions.md` — risk levels, predefined immediate actions, cross-cutting footnotes (read before Steps 9–11).
4. `references/ihr_annex2_decision_instrument.md` — the actual IHR Annex 2 four-criteria decision instrument and always-notifiable disease list, read at Step 11 instead of relying on background knowledge for the footnote (i) check.
5. `references/recording_form_template.md` — field-by-field guidance for the output template (read before Step 13).
6. `references/worked_example.md` — a condensed worked example for calibrating depth and voice (read once, or whenever a fresh example would help).
7. `assets/recording_form_blank.md` — the actual fillable Recording Form structure; copy this into the output at Step 13.
7a. `references/evaluation_form_guide.md` — field-by-field guidance for the Evaluation Form output format; read at Step 13a only when that format was selected at Step 1.
7b. `assets/evaluation_form_blank.md` — the fillable Evaluation Form (Part 1 mirror) structure; copy this into the output at Step 13a when that format was selected.
8. `assets/qira_decision_tree.md` — a Mermaid visual of the full routing logic; render or embed this when a visual aid would help an analyst follow or explain a walk (e.g., a novel or contested path), or when the output itself calls for a diagram.
9. `scripts/extract_docx_comments.py` — used at Step 16 only, when extracting reviewer comments from an annotated Word document. Not needed for a standard assessment run.

---

## Step 1 — Confirm mode

Three modes:

- **Autonomous** — complete the full walk and produce the final Recording Form without pausing. Best for batch processing or when the analyst has already reviewed similar signals.
- **Hybrid (default)** — walk the domains silently, then pause once before final output to present the full routing path, risk level, and any judgement calls (Domain 1 override, novel-hazard classification, assumption use) for analyst confirmation or correction.
- **Interactive** — pause after each domain (or each judgement call) so the analyst can see the reasoning and confirm, correct, or override before continuing. Best for training, novel hazards, or high-stakes signals.

If the user doesn't specify, default to Hybrid and say so.

**Then confirm the output format**, which is a separate axis from mode — any mode can produce either format:

- **Results Recording Form (default)** — the standard WHO Annex 1 output: metadata block, verbatim signal, Part A summary, Part B question-by-question table.
- **Evaluation Form** — a document titled **QIRA Claude Skill Results**, carrying this walk's answers question by question in the same order and lettering as the reviewer's own evaluation form, so a reviewer who completed theirs independently can compare directly. Portrait orientation. This is a **standalone** deliverable: it produces neither the Recording Form nor the reviewer's evaluation section, which reviewers hold themselves. See `references/evaluation_form_guide.md` §8.

The analyst may also hand over a completed Recording Form and ask for the Evaluation Form from it. That is a reformatting job, not a new assessment: transcribe the existing codings, terminal, and confidence rather than re-running the walk — see the guide §8.

Trigger the Evaluation Form on any request for an evaluation form, reviewer form, Part 1 mirror, or output for skill evaluation or reviewer benchmarking. If the analyst doesn't mention output format, use the Recording Form alone and don't ask.

The format choice changes nothing about how the algorithm is walked. Steps 3–12 are identical either way; only Step 13 branches.

## Step 2 — Read references

Load the five reference files above. For a first-time run in a session, read all five; for a subsequent run in the same conversation, a quick re-check of `domains_and_questions.md` §6 (the consolidated routing table) is usually sufficient, since that's the part most prone to being misremembered.

## Step 3 — Parse the signal and define scope

Per `algorithm_essentials.md` §3, the scope statement answers five questions, and it is stated explicitly before Domain 1 is touched:

1. What is the event of interest?
2. Why is it of interest?
3. Which geographical area is affected by this event?
4. Who is or may be affected — which population?
5. Within which timeline are we assessing the risk — what is the forward-looking window?

### 3a. Minimum information gate — ask before walking

Work out which of the five the analyst's input actually settles, then close the gaps **before** answering any algorithm question. Do not open the walk on an assumed scope and correct it later: every "case," "number affected," and "attack rate" downstream is denominated in the population and window set here, so a scope revised mid-walk invalidates the answers already given.

**Three are hard requirements. Never walk the tree without them:**

- **The event (1)** — the hazard and what is happening. Usually supplied by the signal itself.
- **The geographical area (3)** — the jurisdiction being assessed, which is *not* always the jurisdiction the signal describes. A signal about country A may be assessed for risk to country B; if the input leaves this open, ask, because the answer determines whether an importation assumption is needed at all.
- **The population of concern (4)** — a named population, not a jurisdiction standing in for one. "Quebec" is a place; "the general population of Quebec" is a population. Before accepting a population, run the concentration check in 3b — if it fires, the population question becomes a three-way scope choice, asked in this same batch.

**Two can be proposed rather than asked, but must be stated and confirmed:**

- **Why it is of interest (2)** — usually derivable from the signal and the analyst's context. Propose a one-line reading and let the analyst correct it.
- **The forward-looking window (5)** — propose a specific window with a reason, rather than defaulting silently to a generic three months. Anchor it to something real about the hazard where one exists: the end of a vector season, the outer incubation period from last exposure, the close of a mass gathering, the next scheduled surveillance update. **This is load-bearing, not administrative.** In a reviewed run, re-anchoring a generic three-month window to the close of the tick season changed which limb of Question 4.2 could be satisfied and moved the terminal by a level.

**How to ask.** Batch every gap into one short set of questions and stop; do not ask serially across turns, and do not ask about things the input already settles. If the analyst declines to specify, or asks you to proceed regardless, state the scope you are adopting and its basis, record it in the output, and walk on that — an explicit stated default is auditable, a silent one is not.

In Autonomous mode the same gate applies to the three hard requirements: an autonomous run with no stated population is not a fast assessment, it is an unscoped one. Propose items 2 and 5 without pausing, and say plainly in the output that they were proposed rather than supplied.

### 3b. Concentration check — make the scope choice before the walk, not after it

**Trigger.** The signal shows the burden concentrated in an identifiable subpopulation — a group defined by setting (long-term care homes, a shelter, a correctional facility, a school), age, community, occupation, exposure, or sub-region. The rough trigger is one group carrying a large majority of reported cases. It is a prompt for judgement, not a threshold: a group near the line whose share is clearly growing should also trigger it. A steep incidence gradient without a case majority is still flagged, as before, in the equity consideration — unless the analyst asks for it to be treated as a scope question.

**Why this happens here.** Every downstream count is denominated in the Step 3 population. When most of the burden sits in one group, a population-wide scope quietly invites the sub-questions to reason about different populations — contact frequency about the group, health-system load about the whole jurisdiction, barriers about whichever reads as more relevant — and the overall answers end up aggregating across units no one chose. Disclosing that afterwards as an equity caveat describes the problem after it has already shaped the codings. The fix is to make the choice explicitly, before Domain 1.

**The choice.** When the trigger fires, fold it into the 3a question batch — name the group, its share of cases and the source for that share — and offer three options:

1. **Population-wide.** The scope stays at the broader population. The concentration is carried into the output as an equity consideration, and every sub-question that reasons about the group declares it and gives the scoped-population coding alongside (`domains_and_questions.md` §4a).
2. **Subpopulation-scoped.** The scope becomes the group itself, and every case count, attack rate, and capacity judgement is denominated there. State in the scope line what the narrower scope leaves out — notably spread beyond the group — so no reader takes the terminal as a population-wide level.
3. **Two runs.** One walk per population, each internally consistent, reported side by side. Per §4a this is preferred over one walk with blended units whenever the analyst needs both pictures.

Present the options on what question each one answers, **not on which terminal each is likely to produce** — forecasting the levels before the walk anchors the scope decision on the outcome.

**Record it in every mode.** Whenever the check fires, the output's Scope line (or the Evaluation Form's scoped-population field) states the group, its share of cases, the option chosen, and the options not taken. A reader weighing the terminal needs to know that a concentration existed and a scope decision was made about it.

**Autonomous mode.** If the analyst named a population, walk it without pausing and record the check as above. If no population was named, the 3a hard gate already requires asking; include the three options in that question.

**Provenance.** The manual's scope questions (§4.2) ask who is or may be affected; they say nothing about concentrated burden or about choosing between nested populations. This check is the skill's own addition, prompted by reviewer comment C6 — flag it as such if an analyst asks where the rule comes from.

### 3c. Signal text, unit of assessment, and assumptions

**Preserve the analyst's original signal text verbatim** at this point — it goes unedited into the Recording Form's "Original signal" code block at Step 13, regardless of how it gets paraphrased or restructured for the walk itself.

**The population named here sets the unit of assessment for the entire walk.** By default, every "case," "number affected," and "attack rate" in every downstream question is counted in that population — see `domains_and_questions.md` §4a. Every sub-question rationale names the population it reasons about as the walk proceeds, the population is restated explicitly at Step 7, and a consistency sweep across Domains 4 and 5 runs at Step 9 before the terminal is derived.

If the analyst's signal makes a different population the more informative unit (a zoonotic hazard where the animal-side picture is what's actually moving), **raise it here, at scope-setting** — offer either a redefined scope or a second run alongside the first. An analyst may override the default and have the overall answers coded in other units; if they do, document it per §4a's override rules and report what the default coding would have produced. Do not raise the unit question for the first time mid-walk at Domain 4: by then it presents as a coding choice with a two-level swing attached, rather than the scope decision it actually is.

If the user hasn't supplied a predefined high-threat hazard list for their context, note that Domain 1 will default to NO/UNKNOWN unless they supply one (see `algorithm_essentials.md` §4).

**Importation/spillover check**: if the source event is outside the jurisdiction being assessed, or is a zoonotic pathogen not yet confirmed in humans, flag this immediately — per `algorithm_essentials.md` §6.2 and `domains_and_questions.md` §7, QIRA requires an explicit assumption (treat the event as already detected within the jurisdiction) before the tree can be walked at all. State the assumption plainly and get analyst sign-off on it in hybrid/interactive mode before proceeding — this is the single most consequential judgement call in the whole walk, since it determines what every downstream answer is actually conditioned on.

## Step 4 — Domain 1: High-threat hazard

Apply the Domain 1 logic from `domains_and_questions.md` §1. If it resolves YES, the walk skips straight to Question 5.2 — go directly to Step 8. Otherwise continue to Step 5.

## Step 5 — Domain 2: Exposure

Apply §2. Route to Domain 3 (Step 6) or divert to Question 4.1 (Step 7) per the outcome.

## Step 6 — Domain 3: Severity

Apply §3. Always proceeds to Question 4.2, but note which branch (Q3 answer) will be needed for the Domain 5 routing junction in Step 8.

**Settle the denominator before coding Q3 A or B** (`domains_and_questions.md` §3a). Name the population each cited severity statistic is computed over, say whether surveillance for this hazard ascertains mild and subclinical infection, and where it does not, code A and B against infections rather than ascertained cases. Name the measure in the cell: an infection fatality proportion, a case fatality rate among reported cases, and a CFR computed within a severe clinical subset are three different quantities, and the third is the one that inflates Q3. This check is as load-bearing as the Step 3 scope gate — it has moved a terminal by a full level on a live signal.

## Step 7 — Domain 4: Potential spread and scale

Apply §4, using whichever of Question 4.1 or 4.2 applies given the path taken so far. Terminal "Very low" resolves here if Question 4.1 = NO — in that case, skip straight to Step 10 (there's no Domain 5 to walk).

Mandatory checks before recording the overall answer, from `domains_and_questions.md` §4a–4c:

1. **Restate the scoped population and confirm the overall answer is in its units.** Sub-questions may draw on animal, environmental, or other-population evidence; by default the overall answer counts cases in the Step 3 population only. This is the single most common way a walk goes wrong by two risk levels. If a unit override was elected at Step 3, apply it and record it per §4a.
2. **Check that each sub-question names its population.** Every sub-question from Domain 2 onward names its population as it is coded; check it here, where it most often slips. A rationale reasoning about a subgroup, a reservoir, or another jurisdiction says so in the cell and gives the scoped-population coding alongside (§4a). The rule is disclosure: other-population reasoning is often exactly what the manual directs.
3. **State the comparator** — expected baseline, observed figure, and the comparison between them, each sourced. No baseline available means the sub-question is Unknown; it does not mean answer Yes and note the gap.
4. **Code Q4.2 B by tier** (§4c). Use a true attack rate if one exists (Tier 1); otherwise a named spread-intensity proxy with its own comparator (Tier 2). Name the tier and the measure in the cell. Unknown only when neither tier is available — and still never Yes off a raw count.

## Step 8 — Domain 5: Capacity

Apply §5. This is where the walk terminates. Use the **consolidated routing table** in `domains_and_questions.md` §6 to determine the final risk level — track which path led to Question 5.2 (there are several), since the same Yes/No answer to 5.2 maps to different risk levels depending on the path.

## Step 9 — Derive and confirm the risk level

**First, run the population consistency sweep** (`domains_and_questions.md` §4a). It comes before the derivation because a fix it prompts can change a sub-question coding, and the derivation has to read the corrected walk. Check that **Q4.2 A2, Q5.1 A (where reached) and Q5.2 E** are all answered against the same population — the Step 3 scope, unless the cell declares otherwise. For each one:

- Confirm the cell names its population, and that the name is accurate. A rationale asserting that a vulnerability or a caseload "sits within scope" is making a claim to verify, not a label to accept — one reviewed run said exactly that of a barrier the scope arguably did not contain.
- Where one of the three is reasoned against a different population, it must be declared in its cell with the scoped-population coding alongside. An undeclared mismatch is a defect: fix the cell.
- Where the scoped-population coding and the declared coding would give different overall answers for Q4.2, Q5.1 or Q5.2, that is a **`CONFIRM:`** item for Step 12, and its direction and size go into the confidence statement at Step 10.

With the sweep done, **perform the mandatory four-step re-derivation in `domains_and_questions.md` §6a before writing the terminal level anywhere.** State, in writing and as separate steps: the arrival row, the gate letter, the answer at that gate, and the terminal read off the table for that gate-and-answer pair. This is a lookup performed at this moment, not a confirmation of a level formed earlier in the walk. A live run has already reported Low from a gate that maps to Moderate, with the gate correctly labelled — so treat this derivation as a hard control, not a formality.

Then apply the sanity floor: a walk that reached Question 5.1 cannot terminate below Moderate, and Very low is reachable only via Q4.1 = No or gate 5.2a = Yes. A violation means a derivation error, not a surprising finding.

If the derived level conflicts with your analytical read of the event, **do not adjust the terminal** — locate the upstream sub-question responsible, fix its coding if it is genuinely wrong, and re-derive. If the coding is right and the level still feels wrong, that tension is reportable content for the confidence section (Step 10), not grounds for overriding the table.

Finally, state the exact path taken (which domains were walked, which were skipped and why). This is the point at which hybrid-mode analysts should see the full reasoning if they haven't already. If the path was unusual, contested, or would benefit from a visual (a novel hazard, a Domain 1 override decision, or a request to explain the algorithm itself), render or point to `assets/qira_decision_tree.md` alongside the text explanation rather than as a substitute for it.

## Step 10 — Confidence level

Apply Table 1 from `algorithm_essentials.md` §5. Name the specific information gaps or areas of expert agreement/disagreement driving the confidence rating — don't just assert a level.

**State the direction of error, not just its size.** For each judgement call that could reasonably have gone the other way, say which way the alternative coding would move the terminal level and by how much (see `algorithm_essentials.md` §5a). "A different analyst could land elsewhere" is not usable by a reviewer; "coding Q4.2 B against the human baseline instead would give 4.2 = No → gate 5.2b → Low" is. Where several open calls all push the same direction, say so explicitly — that is a systematic lean in the assessment, and it is the most useful thing a confidence statement can tell a reviewer.

## Step 11 — Immediate actions and escalation flag

Select actions per `risk_classification_and_actions.md` §2 — use the analyst's own predefined list if one exists; otherwise use the illustrative menu and flag that a jurisdiction-specific list should be formalized. Apply the cross-cutting footnotes from §3. For footnote (i) — the IHR Annex 2 check — consult `references/ihr_annex2_decision_instrument.md` directly rather than relying on background knowledge: confirm whether the hazard is one of the four always-notifiable diseases, and if not, run the four-criteria assessment and report the result explicitly, independent of the QIRA risk level.

## Step 12 — Confirmation pause (hybrid/interactive only)

Chat messages don't support functional jump-to-anchor links, so don't rely on markdown links (`[text](#anchor)`) to help the analyst navigate back to a specific item — they won't actually scroll-jump in this interface. Instead, use this two-part convention to make judgement calls easy to find and respond to:

1. **Flag inline, at the point it occurs.** Whenever the walk includes an assumption (importation/spillover, §7 of `domains_and_questions.md`), a Domain 1 override (Q1 C), a genuinely uncertain sub-question coding, or a novel/contested classification, tag it right there with a consistent text marker — **`CONFIRM:`** — followed by a short, quotable phrase describing the specific call. No emoji or other decorative markers — plain bold text only.
2. **Consolidate into a numbered checklist before finalizing.** At the confirmation pause, list every flagged item as a numbered list, each one quoting the exact flagged phrase from step 1 in quotation marks (not just describing it generically). This lets the analyst reply with numbers ("2 and 4 look right, change 3 to X") instead of re-reading the full walk to find what needs a decision.

Example of the checklist format:

> **Please confirm or correct:**
> 1. Spillover assumption: *"assuming a human case has been identified"* — reasonable, or should this run as pure animal-only surveillance instead?
> 2. Domain 1 override (Q1 C = Yes): *"novel exposure pathway... full walk gives more actionable detail"* — agree, or prefer the standard skip to 5.2e?
> 3. Q3 severity coded Yes/Unknown: *"clade's human-severity profile isn't established"* — any additional data to firm this up?

In interactive mode, apply step 1 (inline flagging) at each domain as it's walked; step 2's consolidated list becomes a shorter final recap rather than a fresh one, since most items will have already been confirmed along the way.

## Step 13 — Populate the Results Recording Form

Copy the structure from `assets/recording_form_blank.md` and fill it in, using `references/recording_form_template.md` for field-by-field guidance. Populate the metadata block (Assessment reference, Model, Date, Version) and the Original signal code block first — the latter must be the analyst's verbatim text preserved from Step 3. Part B always uses the standing format `Domain | Overall Question | Answer | Rationale` — one row per domain/question actually reached, full domain name and full question text in their respective columns, with influential sub-questions named and described within the Rationale rather than broken into separate rows. When labeling the Question 5.2 row, always include the specific gate (5.2a/b/c/d/e) — see `references/domains_and_questions.md` §6. Every specific fact or claim in a Rationale cell gets a hyperlink — to the signal's own source if restating signal-derived information, or to a freshly verified source for anything external — per the citation-verification rule above.

## Step 13a — Populate the Evaluation Form (when that format was selected)

Read `references/evaluation_form_guide.md` and copy the structure from `assets/evaluation_form_blank.md`. Fill the header block, section 1 (verbatim signal with live hyperlinks), section 2 (the decision path table), section 3 (decision path, risk level, confidence), **section 4 (proposed actions)** and section 5 (other considerations). Reproduce the terminal lookup line unaltered.

Four things about this format are easy to get wrong and worth holding in mind while filling it:

- **The decision-path table has two row types per domain** — a shaded domain row (domain, overall question, main answer, aggregation rule) followed by one row per guiding sub-question, each carrying its own answer beside its own rationale. This split is the whole point of the layout: a reader should never have to match an answer in one cell to a sentence in another. Do not collapse the sub-question rows back into a single stacked cell (guide §4).
- **Every one of the seven questions keeps a domain row, including ones the routing bypassed** — mark those `—` / `Not reached — [routing reason]` and omit their sub-question rows. Sub-questions that do not arise are `n/a` with a one-clause reason, never `NO` and never `UNKNOWN` (guide §6).
- **Two of the aggregation notes formalize questions the manual leaves to judgement** (Q3 and Q5.2). Reproduce the notes verbatim, but keep coding those two by judgement; where the mechanical rule and the coded answer diverge, flag it in the domain row's rationale cell and raise it at the Step 12 pause (guide §7).
- **Q5.2 E is inverted in polarity** — it asks whether major barriers exist, so E = No supports the Main answer Yes. Getting this backwards flips the terminal by a full level.
- **Proposed actions go in their own section 4, never folded into other considerations.** Expert reviewers could not find them when they were embedded in a general block, and marked the output down for it (guide §6).

Everything appearing in both artifacts — reference, scope, assumption, sub-question codings, terminal, confidence — must agree. They are two renderings of one walk.

**Do not reproduce the reviewer's evaluation section** (agreement, component ratings, points of divergence, factual errors, overall judgement). Reviewers hold their own copy; drafting, previewing, or pre-filling any of it does their work for them. Likewise, do not open the document with an instructional line about when to complete it — title, then straight to the header block.

## Step 14 — Present output

Deliver the completed Recording Form. If the walk relied on an importation/spillover assumption, surface that prominently rather than burying it in the "Other considerations" field — it changes how the whole assessment should be read.

## Step 15 — Export a standalone Markdown file (on request)

When the analyst wants the Recording Form as a file for external review (e.g., committing to a repo's `outputs/` folder for colleagues to read), create a standalone `.md` file containing exactly the chat output — metadata block, Original signal code block, Part A, Part B — with no additional commentary. Name it after the Assessment reference (e.g., `QIRA-QC-2026-07-29-LEGIONELLOSIS-v1.md`), so the filename alone identifies the run.

Export the Evaluation Form as its own file, same reference plus an `-EVAL` suffix — keeping it separate from the Recording Form lets a reviewer open it without the fuller document in view, which is what the independent comparison depends on. For a `.docx` deliverable use the `docx` skill; checkbox glyphs (☐/☒) and in-cell hyperlinks both carry over, and this format is **portrait**, not landscape. This file is meant to be committed by the analyst using their own git tooling — this skill does not push to any repository itself, and should not be asked to handle git credentials or tokens.

## Step 16 — Extract reviewer comments from an annotated Word document (on request)

If a colleague has annotated an exported `.docx` version of a Recording Form (e.g., via Word or SharePoint) and the analyst brings the commented file back, use `scripts/extract_docx_comments.py` to pull every comment into Markdown:

```
python3 scripts/extract_docx_comments.py reviewed.docx -o comments.md
```

This extracts each comment's author, date, the exact text it's anchored to, the comment body, and threaded replies (nested under their parent) — no manual re-reading of the Word document required. The script has no third-party dependencies (stdlib `zipfile` + `xml.etree` only) and degrades gracefully to "no comments found" if the document has none. This is an on-demand step, not a live sync — it runs whenever the analyst supplies a commented file, not automatically when SharePoint comments are added.
