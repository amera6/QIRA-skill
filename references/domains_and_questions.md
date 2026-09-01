# QIRA — Domains, Questions, and Routing Logic

**Companion to**: `qira-assessor` SKILL.md.

**Source**: *User manual for the Quick and Immediate Risk Assessment (QIRA) algorithm for Member States*, §3.1–3.2, §5, Fig. 2, Annex 1 (form for responding to questions).

**Read this file at Steps 4–8 of SKILL.md.** It is the algorithm itself: five domains walked in a fixed, unidirectional order, each with an overall question and one or more guiding sub-questions, routing to either the next domain or a terminal risk level. This is a genuine decision tree — do not treat the domains as independently-scored axes. Which domain comes next, and even which sub-question of Domain 4/5 gets asked, depends on the answer just given.

---

## Table of contents
1. Domain 1 — High-threat hazard
2. Domain 2 — Exposure
3. Domain 3 — Severity
4. Domain 4 — Potential spread and scale
5. Domain 5 — Capacity
6. Consolidated routing table
7. Assumption handling for imported/not-yet-occurred events

---

## 1. Domain 1 — High-threat hazard

Assesses whether the hazard is already on the Member State's predefined high-threat list. If so, most of the walk can be skipped.

**Overall Question 1**: Does the signal or event involve a hazard predefined as a high threat in your geographical area?

- **A1** — Is there a predefined list of high-threat hazards for this geographical area? (See `algorithm_essentials.md` §4 for how such lists are built.)
- **B1** — Does the signal/event involve a hazard on that list?
- **C1** — If the hazard *is* on the list, does the team still prefer to walk all subsequent domains anyway? This is a deliberate override: the team may have good reason to assess exposure/severity/spread/capacity in full even for a listed hazard. If elected, **document the justification** in the Results Recording Form — this is flagged in the manual as a decision that needs compelling, stated reasons.

**Routing:**
- **YES** → when (A1=YES AND B1=YES) AND C1=NO. Skip Domains 2–4 entirely; go directly to Question 5.2 (capacity for prevention/control) — *not* 5.1.
- **NO / UNKNOWN** → when (A1=NO OR B1=NO) OR (A1=YES AND B1=YES AND C1=YES). Continue to Domain 2.

**Assumption note**: if the event occurred outside the Member State (potential importation) or the pathogen is circulating in animals without confirmed human spillover, assume detection has already occurred within the Member State before answering — see §7 below. Document the assumption.

---

## 2. Domain 2 — Exposure

Assesses whether further exposure is likely, given current presence of the hazard and exposure mechanisms.

**Overall Question 2**: Is further exposure likely to take place?

- **A2** — Is the hazard still present? (biological/infectious, chemical, or radiological/nuclear)
- **B2** — Can people still be exposed? Consider mode of transmission, infectious period, implemented public health measures, behaviour, and travel/trade movement of people, animals, products, vectors.
- **C2** — Is the potentially-affected population susceptible upon exposure? Consider immunity (vaccination/prior infection) and size of susceptible population; for chemical/radiological hazards, whether concentration exceeds the threshold known to cause adverse effects.

**Routing:**
- **YES** → A2=YES AND B2=YES AND C2=YES. Continue to Domain 3.
- **NO** → A2=NO OR B2=NO OR C2=NO. Skip to Question 4.1 (Domain 4, "significant number currently affected" branch).
- **UNKNOWN** → genuine uncertainty on the overall question. Continue to Domain 3 (uncertainty is treated like YES for routing purposes here).

**Note on low-discrimination answers.** For any event that is currently ongoing, A2 ("is the hazard still present?") is affirmative more or less by definition, so a Yes here carries little information about the specific event. The same is true of A3/B3 for a hazard with a well-known severity profile — coding rabies as severe restates the pathogen, not the signal. This is a property of the WHO algorithm as written, not something this skill can or should fix by answering differently. What the skill *can* do is name it: where a sub-question is affirmative on definitional grounds rather than event-specific evidence, say so in the rationale, so a reader does not mistake a near-automatic Yes for a finding about this event. Flag it as an observation about the algorithm's structure and attribute it as such — the manual does not comment on it.

---

## 3. Domain 3 — Severity

Assesses clinical severity among cases: morbidity, mortality, complications.

**Overall Question 3**: Is the disease likely to be moderate to severe among cases in this population?

- **A3** — Is the case fatality rate (CFR) moderate to high? Consider disease- and context-specific knowledge, including CFR variation by risk group and by treatment/case-management limitations.
- **B3** — Has the disease caused (or is it known to cause) high morbidity? Consider ICU admission proportion, severe complications, long-term sequelae.
- **C3** — Has unusually high morbidity or mortality been observed in *this* signal/event compared with what's previously known for the hazard?

**Routing:** Domain 3 always proceeds to Question 4.2 next — but *which* branch of Question 4.2 downstream capacity routing follows depends on whether Q3 came out YES/UNKNOWN or NO (see the consolidated table in §6; this is one of the places the tree forks on an answer that isn't itself a stop/go decision).

---

## 4. Domain 4 — Potential spread and scale

Examines potential for the hazard to spread further, geographically and in case count.

**Question 4.1** (asked only if Overall Question 2 = NO): Are a significant number of people currently affected, compared with what's usually expected for a similar event?
- **NO** → no further questions; risk level resolves to **Very low**.
- **YES / UNKNOWN** → continue to Question 5.2.

**Question 4.2** (asked only if Overall Question 2 = YES or UNKNOWN): Could a high number of cases or substantial geographical spread be expected in future?

- **A4** — Does the hazard have high potential to spread in nature? (Infectious: transmissibility, incubation period, infectious period, R0/Rt, susceptible population size, proportion asymptomatic, unknown transmission chains. Chemical/nuclear: inherent spread potential.)
- **B4** — Are people likely to have frequent contact with the hazard? Assess by hazard type: social mixing / PHSM compliance (human-to-human); contact with infected animals/wildlife (zoonotic); vector density and contact (vector-borne); social mixing and contaminated water/food consumption (waterborne/foodborne); continued high-level exposure/intake (chemical).
- **C4** — Has a high attack rate been observed relative to population, place, and time period (i.e., unusually rapid spread)?
- **D4** — If transmission route or hazard type (or both) is unknown, has a moderate-to-high number of cases been reported in a short period? For endemic diseases, benchmark against the expected baseline for the period, not raw case counts.

### 4a. Unit of assessment — the overall answer defaults to the scoped population's units

**"A high number of cases" means cases in the population of concern named at Step 3.** This is the strong default and it holds unless the analyst explicitly overrides it.

Sub-questions may legitimately be evaluated in other units — B4 explicitly directs you to assess contact with infected animals and wildlife for zoonotic hazards, so animal-side evidence belongs in B4 and often in A4. But that evidence **informs the sub-questions; by default it does not carry the overall answer.** The overall Question 4.2 answer is about expected cases in, or geographical spread affecting, the scoped population.

Worked contrast, using a wildlife rabies epizootic scoped to humans:

- *Default coding*: A4 and B4 draw on the reservoir picture as the manual directs. The overall 4.2 answer then asks whether a high number of **human** cases is expected: with sustained animal circulation, extensive exposure, and no human cases across two years, the answer is **No** → gate 5.2b.
- *Mixed-unit coding*: reading the animal case count as "cases" and answering 4.2 = Yes routes to 5.1 and inflates the walk by roughly two risk levels. This is the failure mode the default exists to prevent.

**Provenance note.** The manual defines scope at §4.2 and uses "cases" throughout without ever stating that the two are bound. That binding is this skill's own synthesis, not a rule the manual states — flag it as such if an analyst asks why the constraint exists.

**Documented override.** An analyst may direct that the overall answer be coded in different units — for a zoonotic hazard where the animal-side picture is what is actually moving, this can be the more informative run. When they do:

- **The analyst elects it; the skill does not offer it as a routine mid-walk choice.** Raise the option at Step 3, when scope is being set, not as a CONFIRM item at Domain 4 after the walk is underway. Presenting it late converts a scope decision into a coding decision and puts a two-level swing in the analyst's hands without the context to judge it.
- **Record it like any other assumption** — in the Recording Form's "Other considerations" field, per §7's documentation rule, stating the unit used, which questions it applies to, and why.
- **Say what the default would have produced.** Give the terminal the scoped-population coding would have reached, so a reader can see the size of the override's effect.
- **Prefer a second run over a mixed walk.** Where practical, the cleaner answer to "I want both pictures" is two assessments with different populations at Step 3, each internally consistent, rather than one walk with blended units.

The same default governs Question 4.1 ("a significant number of people currently affected"), Domain 3's "cases," and Domain 5's caseload questions.

### 4b. State the comparator before answering

The manual supplies no numeric thresholds for "high number," "significant number," or "high attack rate," and reviewers have specifically objected to answers that assert these without saying what they are measured against. Before coding A4, C4, D4, or Question 4.1, state three things explicitly in the rationale:

1. **The expected baseline** for this hazard, this place, this population, and this period — sourced and hyperlinked like any other external fact.
2. **The observed figure** over the same period and denominator.
3. **The comparison** — the ratio, multiple, or exceedance, in the scoped population's units.

If no baseline can be found, that is an **Unknown to declare, not a gap to reason past**. Writing "no precise baseline was available" and then answering Yes anyway is exactly the failure this rule exists to prevent. Where a baseline is genuinely unavailable, code the sub-question Unknown, say so in the rationale, and let the routing table handle it.

Two cautions when constructing the comparison:

- **Ascertainment.** Rising counts against an expanding surveillance footprint, a new case definition, or a newly established testing program partly measure detection effort, not incidence. Say which you think you are seeing, and on what basis.
- **Control-zone expansion is not outbreak acceleration.** A jurisdiction extending its control or surveillance area into new territory indicates the response is following the hazard; it does not by itself establish that the hazard is accelerating.

**Routing:**
- **YES** → (A4=YES AND B4=YES) OR C4=YES OR D4=YES. Continue to Domain 5.
- Following Q3=NO → Q4.2 answer routes to **Question 5.2** (skipping the health-system-overwhelm question).
- Following Q3=YES/UNKNOWN → Q4.2 answer routes to **Question 5.1** if YES/UNKNOWN, or to **Question 5.2** if NO.

*(See the consolidated table in §6 — this is the densest routing junction in the tree.)*

---

## 5. Domain 5 — Capacity

Assesses measures available to control the event: spread control, clinical management capacity, awareness/RCCE, and vulnerabilities/barriers that undermine any of the above.

**Question 5.1** — Is the health care system likely to be overwhelmed? (Asked only when Q2, Q3, and Q4.2 are all YES or UNKNOWN.)
- **A5** — Are health care systems being (or likely to be) overwhelmed by a rapid rise in cases needing hospitalization/ICU? Consider bed capacity, trained workforce, equipment/medicine/commodity availability; current and projected hospitalization/ICU numbers.
- **YES** if A5=YES.

**Question 5.2** — Are capacities for prevention and control measures in place?
- **B5** — Are effective public health measures available/implemented/ready (surveillance & lab capacity; PHSM including isolation, contact-tracing, quarantine, movement restriction; decontamination/environmental cleaning; product removal; vector control; vaccination; timely diagnosis and treatment; IPC in health care settings)?
- **C5** — Are adequate clinical management capacities and services available and accessible (care pathways, bed capacity, workforce, accessibility, effective therapeutics)?
- **D5** — Is there a high level of public awareness of risks/mitigation among at-risk and affected populations, supported by effective RCCE? Consider whether people know the risks, know signs/symptoms and where to seek care, and whether RCCE is actively improving knowledge/behaviour.
- **E5** — Are there major vulnerabilities or barriers that could undermine effectiveness or uptake of prevention, diagnosis, or clinical management (humanitarian crises, hostilities, natural disasters, concurrent outbreaks, resource shortages, distrust, stigma, discrimination)? **This one calls for expert judgement** — the manual specifically flags that the impact of a vulnerability/barrier depends heavily on context, and it should only be coded as "major" if it significantly hampers response effectiveness.

### 5a. Capacity evidence must be current — date-stamp it

Domain 5 asks what is **available and implemented now**, for this event, within the assessment window. Evidence that a jurisdiction responded competently to a comparable event in the past is a weaker claim and must not be coded as though it were active capacity.

Every piece of evidence cited in B5, C5, or D5 carries its date in the rationale. Then classify it:

- **Active capacity** — documented as in effect during, or established for, the current event and assessment window. This supports a Yes.
- **Precedent** — a protocol, advisory, or operation from a prior event or an earlier period, with no evidence it is currently in force. This supports a *weaker* claim: that the jurisdiction has the know-how and a template. Label it as precedent in the rationale and do not let it alone carry a sub-question to Yes.
- **Unknown** — where currency cannot be established. Say so rather than assuming continuity.

A concrete instance of getting this wrong: a 2023 regional vigilance call with a contact-prophylaxis protocol was cited as B5 evidence of measures in place for a 2026 cluster. A reviewer flagged that three-year gap directly. Standing programs that are documented as ongoing (a recurring vaccination campaign with a current-year operational plan, a permanent surveillance zone) are active capacity and count normally — the test is documented currency, not recency of the source article.

---

## 6. Consolidated routing table

This mirrors Annex 1's "form for responding to questions" — use it as the master routing reference while walking Steps 4–8 of SKILL.md.

**Important**: Question 5.2 is asked at up to **five distinct points** in the tree, and each is a genuinely different capacity gate mapping to a different pair of terminal risk levels. Label which gate you're at (5.2a–5.2e below) rather than just writing "5.2" — conflating them is the single easiest way to mis-resolve a walk.

| Domain | Question | If... | Then go to |
|---|---|---|---|
| 1. High-threat hazard | Q1 | YES | **Question 5.2e** (skip 2–4 entirely) |
| | | NO / UNKNOWN | Domain 2 |
| 2. Exposure | Q2 | YES or UNKNOWN | Domain 3 |
| | | NO | Question 4.1 |
| 3. Severity | Q3 | (any answer) | Question 4.2 |
| 4. Spread and scale | Q4.1 (reached via Q2=NO) | NO | **Terminal: Very low** |
| | | YES / UNKNOWN | **Question 5.2a** |
| | Q4.2 (reached via Q3=NO) | NO | **Question 5.2a** |
| | | YES / UNKNOWN | **Question 5.2b** |
| | Q4.2 (reached via Q3=YES/UNKNOWN) | NO | **Question 5.2b** |
| | | YES / UNKNOWN | Question 5.1 |
| 5. Capacity | Q5.1 | NO | **Question 5.2c** |
| | | YES / UNKNOWN | **Question 5.2d** |
| | **Q5.2a** — reached via Q4.1=YES/UNKNOWN, or Q4.2(Q3=NO branch)=NO | YES | **Terminal: Very low** |
| | | NO / UNKNOWN | **Terminal: Low** |
| | **Q5.2b** — reached via Q4.2(Q3=NO)=YES/UNKNOWN, or Q4.2(Q3=YES/UNKNOWN)=NO | YES | **Terminal: Low** |
| | | NO / UNKNOWN | **Terminal: Moderate** |
| | **Q5.2c** — reached via Q5.1=NO | YES | **Terminal: Moderate** |
| | | NO / UNKNOWN | **Terminal: High** |
| | **Q5.2d** — reached via Q5.1=YES/UNKNOWN | YES | **Terminal: High** |
| | | NO / UNKNOWN | **Terminal: Very high** |
| | **Q5.2e** — reached via Domain 1 Q1=YES | YES | **Terminal: High** |
| | | NO / UNKNOWN | **Terminal: Very high** |

**Reading this table**: Question 5.2 is reached via several different paths, and the *same* yes/no answer to 5.2 maps to a different terminal risk level depending on which path got you there. Always track which entry row you arrived through — don't just look up "5.2 = Yes" in isolation. This is the one place a literal transcription risk exists; when in doubt, re-derive from Fig. 2 in the source manual rather than from memory of a prior run.

### 6a. Mandatory terminal re-derivation

A warning is not a control, and this one has already failed in a live run: an assessment correctly identified its gate as 5.2c, correctly answered Yes, and then reported **Low** where the table says **Moderate**. The gate label was right and the lookup was still wrong.

So before the terminal risk level is written anywhere — not in the Recording Form, not in Part A, not in a chat summary — **stop and perform this derivation explicitly, in writing, as four separate stated steps**:

1. **Arrival row** — which routing-table row delivered you to Question 5.2? State it in full (e.g. "reached via Q5.1 = No").
2. **Gate letter** — which of 5.2a–5.2e does that row correspond to? State the letter.
3. **Answer** — what is the Yes / No-or-Unknown answer at that gate?
4. **Terminal** — read the risk level off the table row for that gate *and* that answer. Quote the mapping (e.g. "5.2c + Yes → Moderate").

Rules governing this derivation:

- **Do it once, at the end, as its own act.** Never carry a terminal level forward from earlier in the walk, from a prior run of a similar signal, or from an expectation formed while reasoning through the domains. The derivation reads the table; it does not confirm a level you already had in mind.
- **The rationale prose must match the derivation.** If a Rationale cell says "gate 5.2c resolves to Low," that sentence is itself the error — check every sentence naming a terminal against step 4 above.
- **A mismatch between the derived terminal and analytical intuition is not resolved by adjusting the terminal.** If the derived level feels wrong, the error is upstream, in a sub-question coding — go back and find it, fix the coding, and re-derive. Silently overriding the table destroys the reproducibility that is QIRA's entire reason for existing.
- **Sanity floor.** Any walk that reaches Question 5.1 can only terminate at Moderate, High, or Very high — reaching 5.1 means Q2, Q3, and Q4.2 all came out Yes or Unknown. A walk that reaches 5.1 and reports Very low or Low has a derivation error by construction. Similarly, Very low is reachable only via Q4.1 = No or gate 5.2a = Yes.

---

## 7. Assumption handling for imported / not-yet-occurred events

Per the manual's Domain 1 note on assumptions (and §6.2 of `algorithm_essentials.md`):

- If the event occurred **outside** the Member State (or subnational area) with import potential: assume it has already been detected inside the Member State (e.g., a case identified at a point of entry or in the community) before walking the tree.
- If a **zoonotic pathogen** is circulating in animals with no confirmed human spillover: assume human cases have been detected before walking the tree.
- Modify question wording as needed to fit the assumption (e.g., Domain 2's question becomes "assuming a case is identified at the airport, is further exposure likely to take place?"), while preserving what the question is actually trying to find out.
- **Document every assumption and every wording modification** explicitly in the Results Recording Form (`recording_form_template.md`) — this is what keeps an assumption-driven run auditable later, and it's the single most important thing to get right when QIRA is stretched to cover an importation or spillover scenario it wasn't natively built to score.
