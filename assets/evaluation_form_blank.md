<!--
QIRA Claude Skill Results — blank template.

Copy this file's structure into the response when the analyst requests the
Evaluation Form output format. For field-by-field guidance and the rules on
rows the routing bypassed, see references/evaluation_form_guide.md.
Sub-question lettering matches this skill throughout
(domains_and_questions.md §0) — no translation needed.

LAYOUT (v1.4.1, replacing the earlier five-column landscape table):
portrait orientation, four columns, and two row types per domain —
  * a shaded DOMAIN ROW carrying the domain name, the overall question, the
    main answer, and the aggregation/routing rule; then
  * one SUB-QUESTION ROW per guiding question, each carrying its own answer
    beside its own rationale.
The point of the split is that a reader never has to match an answer in one
cell to a sentence in another. Do not collapse the sub-question rows back
into a single stacked cell.

Part 2 of the reviewer's document is NOT reproduced here — reviewers hold
their own copy. Never draft, preview, or pre-fill any part of it.

Answers in the decision-path table are written as words (YES / NO /
UNKNOWN / n/a), not checkboxes.
-->

# QIRA Claude Skill Results

| | | | |
|---|---|---|---|
| **Assessment ref.** | | **Date** | |
| **Area of interest / scoped population** | | **Assumption applied** | None (event domestic) / Importation assumed / Spillover assumed |

## 1. Signal (as provided to the skill)

> [paste the analyst's original signal text here, verbatim and unedited, including any linked sources]

## 2. Decision path

| Domain | Questions | Answer | Sub-questions and rationale |
|---|---|---|---|
| **Q1 High-threat hazard** | Does the signal or event involve a hazard predefined as a high threat in your geographical area? | **[Y/N/U]** | *Yes iff A & B yes and C no. Yes → skip to Q5.2* |
| | **A. Predefined list of high-threat hazards exists for the area?** | **[ ]** | |
| | **B. Hazard is on that list?** | **[ ]** | |
| | **C. Team still prefers to assess all domains? (override)** | **[ ]** | |
| **Q2 Exposure** | Is further exposure likely to take place? | **[Y/N/U]** | *Yes iff A, B, C all yes. No → Q4.1; Yes/U → Q3* |
| | **A. Hazard still present?** | **[ ]** | |
| | **B. People can still be exposed?** | **[ ]** | |
| | **C. Population susceptible upon exposure?** | **[ ]** | |
| **Q3 Severity** *(only if Q2 = Y/U)* | Is the disease likely to be moderate to severe among cases in this population? | **[Y/N/U]** | *Yes iff any of A, B, C yes* |
| | **A. CFR moderate to high?** | **[ ]** | |
| | **B. High morbidity (ICU, complications, sequelae)?** | **[ ]** | |
| | **C. Unusually high morbidity/mortality vs. what is known?** | **[ ]** | |
| **Q4.1 Current scale** *(only if Q2 = N)* | Are a significant number of people currently affected? | **[Y/N/U]** | *No → Very low (terminal). Y/U → Q5.2*<br><br>**Comparator:** [expected baseline, observed figure, comparison] |
| **Q4.2 Future spread** *(only if Q2 = Y/U)* | Could a high number of cases or substantial geographical spread be expected in the future? | **[Y/N/U]** | *Yes iff (A1 & A2) or B or C. Q3 & Q4.2 both Y/U → Q5.1; else → Q5.2*<br><br>**Comparator:** [expected baseline, observed figure, comparison — in the scoped population's units, each sourced] |
| | **A1. High potential to spread in nature?** | **[ ]** | |
| | **A2. Frequent contact with the hazard likely?** | **[ ]** | |
| | **B. High attack rate observed (population/place/time)?** | **[ ]** | |
| | **C. Unknown route/hazard AND moderate-to-high cases in short period?** | **[ ]** | |
| **Q5.1 System overwhelmed** *(only if Q2, Q3, Q4.2 all Y/U)* | Is the health care system likely to be overwhelmed? | **[Y/N/U]** | *Yes iff A yes* |
| | **A. Health care system being / likely to be overwhelmed by cases needing hospitalisation or ICU?** | **[ ]** | |
| **Q5.2 Capacities in place** | Are capacities for prevention and control measures in place? | **[Y/N/U]** | *Yes iff B, C, D all yes AND E no* |
| | **B. Effective PH measures available and implemented / ready?** | **[ ]** | |
| | **C. Adequate clinical management capacity accessible?** | **[ ]** | |
| | **D. High public awareness supported by effective RCCE?** | **[ ]** | |
| | **E. Major vulnerabilities or barriers undermining response?** | **[ ]** | |

## 3. Result

| | |
|---|---|
| **Decision path** | Q1 \_\_ → Q2 \_\_ → Q3 \_\_ → Q4.1 \_\_ / Q4.2 \_\_ → Q5.1 \_\_ → Q5.2\_ \_\_ |
| **Risk level** | ☐ Very low ☐ Low ☐ Moderate ☐ High ☐ Very high |
| **Confidence (Table 1)** | ☐ Low ☐ Moderate ☐ High &nbsp; Main information gaps: |

## 4. Proposed actions

| | |
|---|---|
| **Source of actions** | [the analyst's predefined list for this risk level, or "no predefined list supplied — drawn from the QIRA manual's illustrative menu"] |
| **Actions** | [one per line, each an imperative starting with a verb] |
| **Reassessment trigger** | [what would make this assessment invalid before the window closes] |

## 5. Other considerations

| | |
|---|---|
| **IHR (2005) Annex 2** | [four-criteria result, determined independently of the risk level] |
| **Other footnotes** | [cross-border sharing, public concern, novel-hazard judgement, as applicable] |
| **Equity** | [distribution concealed by the scoped average, where relevant] |
| **Signal accuracy** | [any point where the signal's characterisation does not match its underlying source] |
| **Assumptions** | [importation/spillover assumption and any modified question wording] |

**Terminal lookup (Fig. 2):** Q1 Yes → Q5.2 Yes = High / No-U = Very high • Q5.1 Yes-U → Q5.2 Yes = High / No-U = Very high • Q5.1 No → Q5.2 Yes = Moderate / No-U = High • Q2 Y-U but not (Q3 & Q4.2) → Q5.2 Yes = Low / No-U = Moderate • Q2 No, Q4.1 Y-U → Q5.2 Yes = Very low / No-U = Low • Q2 No, Q4.1 No = Very low. "Unknown" always follows the Yes branch.
