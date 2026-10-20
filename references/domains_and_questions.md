# QIRA — Domains, Questions, and Routing Logic

**Companion to**: `qira-assessor` SKILL.md.

**Source**: *User manual for the Quick and Immediate Risk Assessment (QIRA) algorithm for Member States*, §3.1–3.2, §5, Fig. 2, Annex 1 (form for responding to questions).

**Read this file at Steps 4–8 of SKILL.md.** It is the algorithm itself: five domains walked in a fixed, unidirectional order, each with an overall question and one or more guiding sub-questions, routing to either the next domain or a terminal risk level. This is a genuine decision tree — do not treat the domains as independently-scored axes. Which domain comes next, and even which sub-question of Domain 4/5 gets asked, depends on the answer just given.

---

## Table of contents
0. Sub-question labelling convention
1. Domain 1 — High-threat hazard
2. Domain 2 — Exposure
3. Domain 3 — Severity
4. Domain 4 — Potential spread and scale
5. Domain 5 — Capacity
6. Consolidated routing table
7. Assumption handling for imported/not-yet-occurred events

---

## 0. Sub-question labelling convention

**Sub-questions are lettered within their own question, and always cited with that question's number attached.** Domain 2's first sub-question is `Q2 A`, Domain 5's barriers question is `Q5.2 E`. Inside a domain's own section below, the bare letter is enough; anywhere else — Recording Form rationale, Evaluation Form evidence cells, confidence statements, chat narration — carry the question number.

This matters more than a naming convention usually would, because one letter is genuinely ambiguous without it. **`A1` means Question 4.2's first sub-question here, and Domain 1's first sub-question in the WHO manual.** Writing `Q4.2 A1` and `Q1 A` keeps the two apart; writing bare `A1` does not, and a reader who resolves it the wrong way is reading the wrong sub-question.

The WHO manual letters sub-questions globally instead (`A1`–`C1`, `A2`–`C2`, `A3`–`C3`, `A4`–`D4`, `A5`, `B5`–`E5`). This skill does not, so a crosswalk is needed whenever an analyst is reading the manual alongside a skill output:

| This skill | WHO manual | Question |
|---|---|---|
| Q1 A / B / C | A1 / B1 / C1 | High-threat list exists / hazard on it / override elected |
| Q2 A / B / C | A2 / B2 / C2 | Hazard present / exposure possible / population susceptible |
| Q3 A / B / C | A3 / B3 / C3 | CFR / morbidity / unusual severity for this event |
| **Q4.2 A1** | **A4** | High potential to spread in nature |
| **Q4.2 A2** | **B4** | Frequent contact with the hazard likely |
| **Q4.2 B** | **C4** | High attack rate observed |
| **Q4.2 C** | **D4** | Unknown route AND moderate-to-high cases in a short period |
| Q5.1 A | A5 | Health system overwhelmed or likely to be |
| Q5.2 B / C / D / E | B5 / C5 / D5 / E5 | PH measures / clinical management / RCCE / barriers |

Question 4.1 has no sub-questions in either scheme — it is coded directly.

Two things follow. When quoting the manual, quote its labels as printed and give this skill's equivalent alongside rather than silently converting. And when an analyst names a sub-question in an unqualified way, check which scheme they mean before coding against it — the four Q4.2 rows are where a mismatch does real damage, since `A4` and `Q4.2 A1` are the same question under different names while `A1` and `Q4.2 A1` are not.

---

## 1. Domain 1 — High-threat hazard

Assesses whether the hazard is already on the Member State's predefined high-threat list. If so, most of the walk can be skipped.

**Overall Question 1**: Does the signal or event involve a hazard predefined as a high threat in your geographical area?

- **A** — Is there a predefined list of high-threat hazards for this geographical area? (See `algorithm_essentials.md` §4 for how such lists are built.)
- **B** — Does the signal/event involve a hazard on that list?
- **C** — If the hazard *is* on the list, does the team still prefer to walk all subsequent domains anyway? This is a deliberate override: the team may have good reason to assess exposure/severity/spread/capacity in full even for a listed hazard. If elected, **document the justification** in the Results Recording Form — this is flagged in the manual as a decision that needs compelling, stated reasons.

**Routing:**
- **YES** → when (A=YES AND B=YES) AND C=NO. Skip Domains 2–4 entirely; go directly to Question 5.2 (capacity for prevention/control) — *not* 5.1.
- **NO / UNKNOWN** → when (A=NO OR B=NO) OR (A=YES AND B=YES AND C=YES). Continue to Domain 2.

**Assumption note**: if the event occurred outside the Member State (potential importation) or the pathogen is circulating in animals without confirmed human spillover, assume detection has already occurred within the Member State before answering — see §7 below. Document the assumption.

---

## 2. Domain 2 — Exposure

Assesses whether further exposure is likely, given current presence of the hazard and exposure mechanisms.

**Overall Question 2**: Is further exposure likely to take place?

- **A** — Is the hazard still present? (biological/infectious, chemical, or radiological/nuclear)
- **B** — Can people still be exposed? Consider mode of transmission, infectious period, implemented public health measures, behaviour, and travel/trade movement of people, animals, products, vectors.
- **C** — Is the potentially-affected population susceptible upon exposure? Consider immunity (vaccination/prior infection) and size of susceptible population; for chemical/radiological hazards, whether concentration exceeds the threshold known to cause adverse effects.

**Routing:**
- **YES** → A=YES AND B=YES AND C=YES. Continue to Domain 3.
- **NO** → A=NO OR B=NO OR C=NO. Skip to Question 4.1 (Domain 4, "significant number currently affected" branch).
- **UNKNOWN** → genuine uncertainty on the overall question. Continue to Domain 3 (uncertainty is treated like YES for routing purposes here).

**Note on low-discrimination answers.** For any event that is currently ongoing, Q2 A ("is the hazard still present?") is affirmative more or less by definition, so a Yes here carries little information about the specific event. The same is true of Q3 A/B for a hazard with a well-known severity profile — coding rabies as severe restates the pathogen, not the signal. This is a property of the WHO algorithm as written, not something this skill can or should fix by answering differently. What the skill *can* do is name it: where a sub-question is affirmative on definitional grounds rather than event-specific evidence, say so in the rationale, so a reader does not mistake a near-automatic Yes for a finding about this event. Flag it as an observation about the algorithm's structure and attribute it as such — the manual does not comment on it.

---

## 3. Domain 3 — Severity

Assesses clinical severity among cases: morbidity, mortality, complications.

**Overall Question 3**: Is the disease likely to be moderate to severe among cases in this population?

- **A** — Is the case fatality rate (CFR) moderate to high? Consider disease- and context-specific knowledge, including CFR variation by risk group and by treatment/case-management limitations.
- **B** — Has the disease caused (or is it known to cause) high morbidity? Consider ICU admission proportion, severe complications, long-term sequelae.
- **C** — Has unusually high morbidity or mortality been observed in *this* signal/event compared with what's previously known for the hazard?

**Routing:** Domain 3 always proceeds to Question 4.2 next — but *which* branch of Question 4.2 downstream capacity routing follows depends on whether Q3 came out YES/UNKNOWN or NO (see the consolidated table in §6; this is one of the places the tree forks on an answer that isn't itself a stop/go decision).

---

## 4. Domain 4 — Potential spread and scale

Examines potential for the hazard to spread further, geographically and in case count.

**Question 4.1** (asked only if Overall Question 2 = NO): Are a significant number of people currently affected, compared with what's usually expected for a similar event?
- **NO** → no further questions; risk level resolves to **Very low**.
- **YES / UNKNOWN** → continue to Question 5.2.

**Question 4.2** (asked only if Overall Question 2 = YES or UNKNOWN): Could a high number of cases or substantial geographical spread be expected in future?

- **A1** — Does the hazard have high potential to spread in nature? (Infectious: transmissibility, incubation period, infectious period, R0/Rt, susceptible population size, proportion asymptomatic, unknown transmission chains. Chemical/nuclear: inherent spread potential.)
- **A2** — Are people likely to have frequent contact with the hazard? Assess by hazard type: social mixing / PHSM compliance (human-to-human); contact with infected animals/wildlife (zoonotic); vector density and contact (vector-borne); social mixing and contaminated water/food consumption (waterborne/foodborne); continued high-level exposure/intake (chemical).
- **B** — Has a high attack rate been observed relative to the population, place, and time period? The manual adds that this *includes* situations where the signal or event shows unusually rapid spread of incident cases — so attack rate is the named measure, not the only admissible one. Code it by the two tiers in §4c.
- **C** — If transmission route or hazard type (or both) is unknown, has a moderate-to-high number of cases been reported in a short period?

**Manual note following B and C:** for endemic diseases, use the expected numbers in a period as the baseline; surveillance data can establish trends and trajectories to show whether case numbers are unusual. (That raw counts never carry a Yes on their own is this skill's §4b rule, not wording from the manual.)

### 4a. Unit of assessment — the overall answer defaults to the scoped population's units

**"A high number of cases" means cases in the population of concern named at Step 3.** This is the strong default and it holds unless the analyst explicitly overrides it.

Sub-questions may legitimately be evaluated in other units — Q4.2 A2 explicitly directs you to assess contact with infected animals and wildlife for zoonotic hazards, so animal-side evidence belongs in Q4.2 A2 and often in Q4.2 A1. But that evidence **informs the sub-questions; by default it does not carry the overall answer.** The overall Question 4.2 answer is about expected cases in, or geographical spread affecting, the scoped population.

Worked contrast, using a wildlife rabies epizootic scoped to humans:

- *Default coding*: Q4.2 A1 and A2 draw on the reservoir picture as the manual directs. The overall 4.2 answer then asks whether a high number of **human** cases is expected: with sustained animal circulation, extensive exposure, and no human cases across two years, the answer is **No** → gate 5.2b.
- *Mixed-unit coding*: reading the animal case count as "cases" and answering 4.2 = Yes routes to 5.1 and inflates the walk by roughly two risk levels. This is the failure mode the default exists to prevent.

**Provenance note.** The manual defines scope at §4.2 and uses "cases" throughout without ever stating that the two are bound. That binding is this skill's own synthesis, not a rule the manual states — flag it as such if an analyst asks why the constraint exists.

**Documented override.** An analyst may direct that the overall answer be coded in different units — for a zoonotic hazard where the animal-side picture is what is actually moving, this can be the more informative run. When they do:

- **The analyst elects it; the skill does not offer it as a routine mid-walk choice.** Raise the option at Step 3, when scope is being set, not as a CONFIRM item at Domain 4 after the walk is underway. Presenting it late converts a scope decision into a coding decision and puts a two-level swing in the analyst's hands without the context to judge it.
- **Record it like any other assumption** — in the Recording Form's "Other considerations" field, per §7's documentation rule, stating the unit used, which questions it applies to, and why.
- **Say what the default would have produced.** Give the terminal the scoped-population coding would have reached, so a reader can see the size of the override's effect.
- **Prefer a second run over a mixed walk.** Where practical, the cleaner answer to "I want both pictures" is two assessments with different populations at Step 3, each internally consistent, rather than one walk with blended units.

The same default governs Question 4.1 ("a significant number of people currently affected"), Domain 3's "cases," and Domain 5's caseload questions.

#### Every sub-question names the population it reasons about

The default above binds the **overall** answers. It is not enough on its own, because sub-question rationales can drift between populations without the overall answer visibly changing — and when they drift in different directions, the aggregation is combining units nobody chose. So from Domain 2 onward, **each sub-question rationale names the population it is reasoning about**, in a few words at the start of the cell:

> *Scoped population (general population of Ontario):* …
> *LTC residents — subgroup of scoped population:* … *Scoped-population coding:* No — …
> *Raccoon reservoir — not the scoped population:* … *Scoped-population coding:* …

Where the population named **differs from the Step 3 scope — including a subgroup inside it** — say so in the cell and give the scoped-population coding alongside. Domain 1's sub-questions are exempt: they ask about a list and a team decision, not about a population.

This is a **disclosure rule, not a prohibition.** Reasoning about another population is often exactly what the manual directs. Q3 A tells the assessor to consider CFR among high-risk groups, and the manual's own worked example (Annex 2, dengue) codes Q3 A Yes on a 12% CFR in children aged 0–10 against 0.5% overall. Q4.2 A2 directs zoonotic assessments to contact with animals. The Answer column still carries the coding the rationale argues for. What the rule adds is the scoped-population coding beside it, so a reader can see whether the choice of population carried the answer. Where the two codings would give different **overall** answers, raise it as a `CONFIRM:` item and state its direction per `algorithm_essentials.md` §5a.

**Provenance note.** The manual asks that the scope be defined (§4.2) and supplies the high-risk-group consideration in Q3 A; it does not ask that sub-question rationales name their population. The naming rule and the sweep below are this skill's own controls, added after reviewer comment C6.

#### Population consistency sweep — before the terminal is derived

After Domain 5 and before the §6a re-derivation (SKILL.md Step 9), check that **Q4.2 A2, Q5.1 A (where reached) and Q5.2 E** are all answered against the same population. These three are singled out because their subject slides easily between a concentrated group and the whole jurisdiction: contact frequency, hospital load, and barriers to response. In the reviewed run that prompted this rule, Q5.1 declared its dependency on the scope, Q4.2 A2 did not, and Q5.2 E asserted that a vulnerability sat squarely within a scope it arguably did not.

- **Any of the three not answered against the Step 3 scope is declared** in its own cell, with the scoped-population coding alongside. An undeclared mismatch is a defect: correct the cell before the terminal is derived.
- **Test claims of scope membership, don't just look for a label.** "Sits within scope" is itself an assertion about who the evidence describes.
- **The sweep runs before the derivation, not after it**, because a correction can change a sub-question coding and therefore the terminal.

Other sub-questions found reasoning about a different population are declared the same way; the three above are the ones that must be checked every time.

### 4b. State the comparator before answering

The manual supplies no numeric thresholds for "high number," "significant number," or "high attack rate," and reviewers have specifically objected to answers that assert these without saying what they are measured against. Before coding Q4.2 A1, B, C, or Question 4.1, state three things explicitly in the rationale:

1. **The expected baseline** for this hazard, this place, this population, and this period — sourced and hyperlinked like any other external fact.
2. **The observed figure** over the same period and denominator.
3. **The comparison** — the ratio, multiple, or exceedance, in the scoped population's units.

If no baseline can be found, that is an **Unknown to declare, not a gap to reason past**. Writing "no precise baseline was available" and then answering Yes anyway is exactly the failure this rule exists to prevent. Where a baseline is genuinely unavailable, code the sub-question Unknown, say so in the rationale, and let the routing table handle it. For Q4.2 B, "unavailable" means unavailable at both tiers of §4c — check for a named spread-intensity proxy with its own comparator before declaring Unknown.

Two cautions when constructing the comparison:

- **Ascertainment.** Rising counts against an expanding surveillance footprint, a new case definition, or a newly established testing program partly measure detection effort, not incidence. Say which you think you are seeing, and on what basis.
- **Control-zone expansion is not outbreak acceleration.** A jurisdiction extending its control or surveillance area into new territory indicates the response is following the hazard; it does not by itself establish that the hazard is accelerating.

### 4c. Coding Q4.2 B — attack rate first, a named spread-intensity proxy second

**What B is asking.** Whether transmission is occurring faster or more intensely than expected for this population, place and period. The manual names attack rate as the measure, and its own wording extends B to signals showing unusually rapid spread of incident cases. Attack rate is therefore the preferred measure, not the only admissible one. Without this reading, B defaults to Unknown for almost every real signal, because true attack rates with a stated denominator are rarely published early in an event.

**Tier 1 — a true attack rate.** Cases over a stated population at risk, over a stated period, in the scoped population (or in a subgroup declared per §4a). Compare it with an expected baseline per §4b. Where a Tier 1 measure exists, it governs the coding. Tier 2 evidence may be reported beside it but does not override it; if the two point in different directions, say so.

**Tier 2 — a named proxy for spread intensity**, used only when no Tier 1 measure is available:

- **Epidemic growth rate or doubling time**, compared with what is expected for this hazard, place and season.
- **Secondary attack rate among traced contacts**, compared with the hazard's established secondary attack rate from an authoritative source. Do not compare it with population background incidence — that is a comparison across differently constructed denominators, the exact characterization failure SKILL.md's citation section describes.
- **Notification rate against the same-period baseline** — for example, the same weeks in prior seasons. This is the manual's endemic-disease note applied to B.

**Coding rules, both tiers:**

- **Label the tier and the measure in the cell** — `Tier 1 (attack rate, per 100,000, weeks 30–35)` or `Tier 2 (doubling time)` — so a reader can see what the answer rests on.
- **Every Tier 2 measure needs its own §4b comparator** — expected value, observed value, comparison, each sourced. A proxy without a comparator is not Tier 2; it is a count with a label on it.
- **Still no Yes off a raw count.** A count with neither a denominator nor a baseline belongs to neither tier.
- **The ascertainment caution in §4b bites hardest here.** Growth rates, doubling times and notification rates computed from notifications all rise with testing effort and case-definition changes. Say which you think you are seeing, and on what basis.
- **Unknown only when neither tier is available.**

**Provenance note.** The manual supplies B's wording and the endemic baseline note. The ordering into tiers, the proxy list, and the rule that Tier 1 governs when present are this skill's own synthesis, added after reviewer comment C7. Flag them as such if asked.

**Open design question — not resolved in this version.** The manual's rule states only when Q4.2 is **Yes**: A1 and A2 both yes, or B or C yes. It does not say whether Q4.2 is No or Unknown when no limb is Yes but a sub-question is Unknown. That difference changes the terminal, because Unknown routes like Yes (§6). Until the analyst sets a rule, **do not resolve it silently**. When it arises, raise it as a `CONFIRM:` item, give the route and terminal under each reading, and carry both into the confidence statement.

**Routing:**
- **YES** → (A1=YES AND A2=YES) OR B=YES OR C=YES. Continue to Domain 5.
- Following Q3=NO → Q4.2 answer routes to **Question 5.2** (skipping the health-system-overwhelm question).
- Following Q3=YES/UNKNOWN → Q4.2 answer routes to **Question 5.1** if YES/UNKNOWN, or to **Question 5.2** if NO.

*(See the consolidated table in §6 — this is the densest routing junction in the tree.)*

---

## 5. Domain 5 — Capacity

Assesses measures available to control the event: spread control, clinical management capacity, awareness/RCCE, and vulnerabilities/barriers that undermine any of the above.

**Question 5.1** — Is the health care system likely to be overwhelmed? (Asked only when Q2, Q3, and Q4.2 are all YES or UNKNOWN.)
- **A** — Are health care systems being (or likely to be) overwhelmed by a rapid rise in cases needing hospitalization/ICU? Consider bed capacity, trained workforce, equipment/medicine/commodity availability; current and projected hospitalization/ICU numbers.
- **YES** if A=YES.

**Question 5.2** — Are capacities for prevention and control measures in place?
- **B** — Are effective public health measures available/implemented/ready (surveillance & lab capacity; PHSM including isolation, contact-tracing, quarantine, movement restriction; decontamination/environmental cleaning; product removal; vector control; vaccination; timely diagnosis and treatment; IPC in health care settings)?
- **C** — Are adequate clinical management capacities and services available and accessible (care pathways, bed capacity, workforce, accessibility, effective therapeutics)?
- **D** — Is there a high level of public awareness of risks/mitigation among at-risk and affected populations, supported by effective RCCE? Consider whether people know the risks, know signs/symptoms and where to seek care, and whether RCCE is actively improving knowledge/behaviour.
- **E** — Are there major vulnerabilities or barriers that could undermine effectiveness or uptake of prevention, diagnosis, or clinical management (humanitarian crises, hostilities, natural disasters, concurrent outbreaks, resource shortages, distrust, stigma, discrimination)? **This one calls for expert judgement** — the manual specifically flags that the impact of a vulnerability/barrier depends heavily on context, and it should only be coded as "major" if it significantly hampers response effectiveness.

### 5a. Capacity evidence must be current — date-stamp it

Domain 5 asks what is **available and implemented now**, for this event, within the assessment window. Evidence that a jurisdiction responded competently to a comparable event in the past is a weaker claim and must not be coded as though it were active capacity.

Every piece of evidence cited in Q5.2 B, C, or D carries its date in the rationale. Then classify it:

- **Active capacity** — documented as in effect during, or established for, the current event and assessment window. This supports a Yes.
- **Precedent** — a protocol, advisory, or operation from a prior event or an earlier period, with no evidence it is currently in force. This supports a *weaker* claim: that the jurisdiction has the know-how and a template. Label it as precedent in the rationale and do not let it alone carry a sub-question to Yes.
- **Unknown** — where currency cannot be established. Say so rather than assuming continuity.

A concrete instance of getting this wrong: a 2023 regional vigilance call with a contact-prophylaxis protocol was cited as Q5.2 B evidence of measures in place for a 2026 cluster. A reviewer flagged that three-year gap directly. Standing programs that are documented as ongoing (a recurring vaccination campaign with a current-year operational plan, a permanent surveillance zone) are active capacity and count normally — the test is documented currency, not recency of the source article.

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
