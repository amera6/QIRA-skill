# QIRA — Results Recording Form Template

**Companion to**: `qira-assessor` SKILL.md. Read at Step 13 (populate output) and use as the literal output structure.

**Source**: *QIRA User Manual*, Annex 1. Member States may adapt this form to local needs — the fields below are the WHO-suggested default; note any deviation the analyst's context requires.

---

## Part A — Summary form

- **Signal/event:**
- **Member State / subnational area:**
- **Date of quick and immediate risk assessment:**
- **Version:** (increment on each reassessment)
- **Brief summary of signal or event and scope of assessment:** time, place, person; what the event is and why it's of interest; geographical area and population in scope; forward-looking window (valid until when, absent major change).
- **Risk level classification:** [Very low | Low | Moderate | High | Very high]
- **Rationale:** the specific findings that drove the routing outcome — name the domains and sub-questions that determined the path, not a generic restatement of the risk level.
- **Confidence level:** [Low | Moderate | High] with the specific information gaps or expert-agreement basis (Table 1 in `algorithm_essentials.md` §5).
- **Proposed actions:** drawn from the Member State's predefined list where one exists (see `risk_classification_and_actions.md` §2); note explicitly if none exists and a generic menu was used instead.
- **Other considerations:** any footnote-level items from `risk_classification_and_actions.md` §3 that apply (IHR notification flag, cross-border sharing, political sensitivity, novel-hazard judgement call), and any assumptions made per `domains_and_questions.md` §7 (importation/spillover assumption, modified question wording).

## Part B — Question-by-question response form

Reproduce this table with every question actually asked during the walk (skip rows for questions the routing logic bypassed, but keep a one-line note on *why* they were skipped):

| Domain | Algorithm question | Assessment (Yes/No/Unknown) | Notes |
|---|---|---|---|
| 1. High-threat hazard | Does the signal/event involve a hazard predefined as a high threat in your geographical area? | | If yes → 5.2. If no/unknown → Domain 2. |
| 2. Exposure | Is further exposure likely to take place? | | If yes/unknown → Domain 3. If no → 4.1. |
| 3. Severity | Is the disease likely to be moderate to severe among cases in this population? | | → 4.2. |
| 4.1 Spread and scale | Are a significant number of people currently affected? | | If no → terminal (Very low). If yes/unknown → 5.2. |
| 4.2 Spread and scale | Could a high number of cases or substantial geographical spread be expected in future? | | Routes to 5.1 or 5.2 depending on Q3 (see `domains_and_questions.md` §6). |
| 5.1 Capacity | Is the health care system likely to be overwhelmed? | | → 5.2. |
| 5.2 Capacity | Are capacities for prevention and control measures in place? | | Terminal — resolves risk level per §6 routing table. |

For each row actually populated, carry the sub-question findings (A1/B1/C1, A2/B2/C2, etc.) as brief supporting notes — these are what the Part A "Rationale" field draws from.

## Compatibility note

This is a working paper-trail document, not a formatted deliverable by default — render it as a clean markdown table/summary unless the analyst asks for a specific downstream format (e.g., inserting into a Word template or a specific bulletin field).
