# QIRA — Algorithm Essentials

**Companion to**: `qira-assessor` SKILL.md (read in Step 2's reference order).

**Source**: *User manual for the Quick and Immediate Risk Assessment (QIRA) algorithm for Member States*. Geneva: World Health Organization; 2025. This file extracts the framing, scope-setting, confidence, and limitations material an analyst needs before and after running the algorithm itself — the algorithm's question-by-question logic lives in `domains_and_questions.md`, and risk levels/actions live in `risk_classification_and_actions.md`.

---

## 1. What QIRA is for

QIRA is a **quick, immediate** risk assessment tool for events already verified (or in urgent cases, prior to verification) within public health intelligence (PHI) activities. It is meant for use by the team already doing routine detection/verification — not a multidisciplinary panel — and produces two things: a risk level (very low → very high) and a set of immediate actions drawn from a Member State's own predefined list.

**QIRA vs. MS-RRA** — the two tools are sequential, not competing:

| | QIRA | MS-RRA |
|---|---|---|
| Completion time | Under 1 hour | Typically several days |
| Team | Routine detection/verification team | Multidisciplinary team |
| Question format | Yes/No/Unknown, hierarchical, unidirectional | Six guiding questions per axis, described then coded |
| Output | Risk level + predefined immediate actions | Risk level (optional) + event-specific actions + documented information gaps |
| Trigger for the other | A moderate/high/very-high QIRA result is itself an indicative criterion for initiating MS-RRA | — |

Both tools trace back to WHO's 2012 *Rapid risk assessment of acute public health events* manual. QIRA originated at WHO's South-East Asia Regional Office (building on Western Pacific and ECDC tools), was globalized in 2024 via a 19-Member-State survey, and piloted in six Member States before this version.

## 2. Glossary (shared vocabulary with MS-RRA)

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

## 6. Limitations — read before applying to novel scenarios

**6.1 Methodological.** QIRA is deliberately blunt: fixed yes/no/unknown questions, predefined generic actions per risk level. It won't capture nuance or fit every specific scenario. When an event may have serious public health implications, escalate to MS-RRA for a more comprehensive assessment rather than stretching QIRA past its design intent.

**6.2 Importation and spillover — the load-bearing limitation.** QIRA **cannot estimate the likelihood of a hazard being imported** into the Member State, and **cannot estimate the likelihood of zoonotic spillover** to humans. It can still be used to assess a hazard that hasn't yet reached the human population *within* the Member State — but only by making an explicit assumption first: **assume the event has already affected the population** (e.g., assume a case has been detected at a point of entry or in the community), then answer the algorithm's questions against that assumption. Modify question wording to fit the assumption if needed (e.g., "assuming a case is identified at the airport, is further exposure likely to take place"), while preserving the question's intended information target.

Any such assumption, and any question wording changes made to accommodate it, **must be documented explicitly** in the Results Recording Form. This is not optional bookkeeping — it's the only thing that keeps an assumption-driven QIRA run legible to someone reviewing it later.

**6.3 Disasters and complex emergencies.** QIRA is not designed to estimate an overall risk level for a disaster or complex emergency involving multiple simultaneous hazards. It remains appropriate for assessing a *specific* acute public health event occurring within that context — e.g., a cholera outbreak following a flood, or a measles outbreak in a displacement camp after a typhoon — one hazard at a time.

## 7. IHR (2005) notification

Notification decisions under IHR (2005) Annex 2 (as amended by WHA77.17) are **never conditional** on QIRA's results — that determination runs independently. QIRA's findings can, however, usefully inform an Annex 2 assessment, since QIRA's content is aligned with the Annex 2 considerations.

## 8. Updating an assessment

Repeat the assessment when the epidemiological or contextual situation changes materially, or when confidence in the current assessment is not high and new information becomes available. For events with serious implications, consider moving to MS-RRA at the point of reassessment rather than repeating QIRA indefinitely.
