# QIRA — Algorithm Essentials

**Companion to**: `qira-assessor` SKILL.md (read in Step 2's reference order).

**Source**: *User manual for the Quick and Immediate Risk Assessment (QIRA) algorithm for Member States*. Geneva: World Health Organization; 2025. This file extracts the framing, scope-setting, confidence, and limitations material an analyst needs before and after running the algorithm itself — the algorithm's question-by-question logic lives in `domains_and_questions.md`, and risk levels/actions live in `risk_classification_and_actions.md`.

---

## 1. What QIRA is for

QIRA is a **quick, immediate** risk assessment tool for events already verified (or in urgent cases, prior to verification) within public health intelligence (PHI) activities. It is meant for use by the team already doing routine detection/verification, and produces two things: a risk level (very low → very high) and a set of immediate actions drawn from a jurisdiction's own predefined list.

It is a self-contained, hierarchical yes/no/unknown decision tree: each question's answer determines the next question, and the walk terminates at a risk level with no separate scoring or averaging step. This skill treats QIRA on its own terms — its logic doesn't depend on, or feed into, any other assessment framework.

QIRA traces back to WHO's 2012 *Rapid risk assessment of acute public health events* manual. It originated at WHO's South-East Asia Regional Office (building on Western Pacific and ECDC tools), was globalized in 2024 via a 19-Member-State survey, and piloted in six Member States before this version.

## 2. Glossary

- **Signal** — data/information considered to represent a potential acute risk to human health, from any source.
- **Event** — a signal that has been verified (validity/veracity cross-checked).
- **Hazard** — any biological, chemical, or physical agent with potential to cause adverse health effects.
- **Response capacity** — a system's capacity to mitigate risk by reducing likelihood and/or impact.
- **Confidence** — how sure the team is of an estimate; distinct from inherent variability, which persists even with perfect information.
- **Risk** — the likelihood of occurrence and likely magnitude of consequences of an adverse event over a specified period.

## 3. Before running the algorithm: define the scope

Per §4.2, the team should agree on scope before starting:

- What is the event of interest?
- Why is it of interest?
- Which geographical area is affected?
- Who is or may be affected (which population)?
- What is the forward-looking window for the assessment?

This scope statement feeds directly into the Results Recording Form's summary field (see `recording_form_template.md`) and should be captured once per assessment, before Domain 1.

## 4. Defining high-threat hazards (feeds Domain 1)

Each Member State (or subnational team) should maintain its own predefined list of high-threat hazards — this is a local artifact, not something QIRA ships with. Build it from:

- IHR (2005) Annex 2, as amended by WHA77.17 (2024) — the always-notifiable diseases (smallpox, poliomyelitis, novel-subtype influenza, SARS, unexplained severe acute respiratory illness with international spread potential) are a reasonable floor.
- WHO's list of chemicals of public health concern.
- Hazards surfaced through a Member State's STAR (Strategic Tool for Assessing Risks) preparedness process.

Infectious, chemical, and radiological/nuclear hazards can all appear on the list. If no list exists for the geographical area in question, Domain 1 defaults to NO and the walk proceeds through all domains.

## 5. After running the algorithm: confidence level

Report a confidence level alongside the risk level, using Table 1:

| Level | Definition | Uncertainty | Typical criteria |
|---|---|---|---|
| **High** | Additional data unlikely to change the result | Low | Few information gaps; general expert agreement; low or well-characterized natural variability |
| **Moderate** | Additional data likely to change the assessment | Moderate | Some information gaps, not necessarily key ones; some expert agreement on key aspects; moderate variability |
| **Low** | Additional data very likely to change the assessment | High | Critical gaps in key information; low expert agreement; novel event type; high or poorly-characterized variability |

### 5a. Reporting confidence usefully — direction, not just magnitude

Table 1 gives the level. What makes the level usable to a reviewer is stating **which way the assessment would move** if the open questions resolved differently. Three requirements, all added after expert review found the previous format insufficient:

- **Name the alternative coding and its terminal.** For each judgement call that could reasonably have gone the other way, give the sub-question, the alternative answer, the resulting route, and the resulting risk level — "coding C4 against the human baseline instead gives 4.2 = No → gate 5.2b → Low." Vague acknowledgement that reasonable analysts might differ tells a reviewer nothing they can check.
- **Say when the open calls lean the same way.** If every unresolved judgement would push the terminal down (or up), that is a systematic lean, and it is more important than the confidence label itself. Reviewers will otherwise find it themselves, one comment at a time.
- **Source trajectory claims like any other fact.** Statements about where a situation is heading — "accelerating," "still rising," "plateauing," "expanding" — are empirical claims subject to the same verification and hyperlinking rules as static facts, and they are easy to overstate. Distinguish growth in the hazard from growth in detection or in the area under surveillance; a jurisdiction extending control operations into new territory is evidence the response is following the hazard, not evidence the hazard is accelerating. Where the direction genuinely isn't established, say the situation is ongoing and leave it there.

A confidence section that does these three things lets a reviewer disagree precisely. One that doesn't forces them to reconstruct the walk to find out what would have changed.

## 6. Limitations — read before applying to novel scenarios

**6.1 Methodological.** QIRA is deliberately blunt: fixed yes/no/unknown questions, predefined generic actions per risk level. It won't capture nuance or fit every specific scenario. When an event may have serious public health implications, a more comprehensive, multidisciplinary rapid risk assessment process is warranted rather than stretching QIRA past its design intent — QIRA is built for speed, not depth.

**6.2 Importation and spillover — the load-bearing limitation.** QIRA **cannot estimate the likelihood of a hazard being imported** into the Member State, and **cannot estimate the likelihood of zoonotic spillover** to humans. It can still be used to assess a hazard that hasn't yet reached the human population *within* the Member State — but only by making an explicit assumption first: **assume the event has already affected the population** (e.g., assume a case has been detected at a point of entry or in the community), then answer the algorithm's questions against that assumption. Modify question wording to fit the assumption if needed (e.g., "assuming a case is identified at the airport, is further exposure likely to take place"), while preserving the question's intended information target.

Any such assumption, and any question wording changes made to accommodate it, **must be documented explicitly** in the Results Recording Form. This is not optional bookkeeping — it's the only thing that keeps an assumption-driven QIRA run legible to someone reviewing it later.

**6.3 Disasters and complex emergencies.** QIRA is not designed to estimate an overall risk level for a disaster or complex emergency involving multiple simultaneous hazards. It remains appropriate for assessing a *specific* acute public health event occurring within that context — e.g., a cholera outbreak following a flood, or a measles outbreak in a displacement camp after a typhoon — one hazard at a time.

## 7. IHR (2005) notification

Notification decisions under IHR (2005) Annex 2 (as amended by WHA77.17) are **never conditional** on QIRA's results — that determination runs independently. QIRA's findings can, however, usefully inform an Annex 2 assessment, since QIRA's content is aligned with the Annex 2 considerations. See `references/ihr_annex2_decision_instrument.md` for the actual decision instrument — don't reason about Annex 2 from background knowledge alone.

## 8. Updating an assessment

Repeat the assessment when the epidemiological or contextual situation changes materially, or when confidence in the current assessment is not high and new information becomes available. For events with serious implications, consider whether a more comprehensive assessment process is warranted at the point of reassessment rather than repeating QIRA indefinitely.
