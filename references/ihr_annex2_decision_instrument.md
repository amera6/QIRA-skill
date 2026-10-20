# IHR (2005) Annex 2 — Decision Instrument

**Companion to**: `qira-assessor` SKILL.md. Read at Step 11 (footnote (i) — IHR Annex 2 check) instead of relying on background knowledge alone.

**Source and provenance**: Core structure verified against *WHO Guidance for the Use of Annex 2 of the International Health Regulations (2005)* (WHO/HSE/IHR/2010.4) and the consolidated IHR (2005) text as amended in 2014, 2022, and 2024 (in force 19 September 2025). This reflects the original 2005 Annex 2 decision instrument, corroborated by CDC and academic sources describing the same structure as of 2024–2025.

**Known gap — read before treating this as authoritative**: the 2024 amendments (WHA77.17) technically amended Annex 2 among several other annexes, primarily to introduce the new "pandemic emergency" category alongside PHEIC. I was not able to fully confirm from primary text whether the core four-criteria instrument or the notifiable-disease lists changed in substance as a result. **Verify against the current official IHR text before relying on this for a real notification decision** — this file is fit for QIRA's purpose (flagging that an Annex 2 check is warranted, and giving enough structure to reason about it), not as a substitute for the primary legal text in an actual notification.

---

## 1. Two categories of notifiable events

**Category A — the four always-notifiable diseases.** Any single case of any of the following, regardless of context, must always be notified to WHO within 24 hours of assessment:

- Smallpox
- Poliomyelitis due to wild-type poliovirus
- Human influenza caused by a new subtype
- Severe Acute Respiratory Syndrome (SARS)

These four are treated as inherently unusual/unexpected with serious public health impact by definition — no further criteria assessment is needed to trigger notification, though the decision instrument should still be applied for events involving *suspected* (not yet confirmed) cases of these diseases.

**Category B — events meeting ≥2 of 4 situational criteria.** All other events must be assessed against the four criteria in §2 below. A specific list of epidemic-prone diseases must *always* be run through this assessment (though a case doesn't automatically trigger notification the way Category A does): cholera, pneumonic plague, yellow fever, viral haemorrhagic fevers (Ebola, Lassa, Marburg), West Nile fever, and other diseases of special national or regional concern (the manual gives dengue fever, Rift Valley fever, and meningococcal disease as examples — this list is deliberately open-ended, not exhaustive).

Beyond Category A and B's named diseases, the assessment applies to *any* event — biological, chemical, or radionuclear, known or unknown agent, natural or intentional — that might meet the four criteria. This is a deliberate design choice in the 2005 revision: notification is event-based, not tied to a fixed disease list.

## 2. The four criteria

Apply these to any event not covered by Category A. **Two or more "yes" answers → notify.**

**Criterion I — Serious public health impact.** Weighs immediate and potential future consequences.
- Is the number of cases/deaths large for the given place, time, or population?
- Does the event have potential for high public health impact? (contributing factors: high epidemic potential, treatment/vaccine/antidote failure, risk even with few cases so far, cases among health staff, especially vulnerable population, factors hindering response like conflict or disaster, high population density, spread of hazardous material)
- Is external assistance needed to detect, investigate, respond to, or control the event?

**Criterion II — Unusual or unexpected nature.**
- Is the event unusual (unknown causal agent/source/route, more severe evolution than typical, unusual for the area/season/population)?
- Is the event unexpected (disease already eliminated/eradicated in the area, or not previously reported there)?

**Criterion III — Significant risk of international spread.**
- Is there an epidemiological link to similar events in other states?
- Any factor alerting to potential cross-border movement of the agent, vehicle, or host? (e.g., an index case with recent international travel or contact with a highly mobile population, environmental contamination with cross-border spread potential, occurrence in an area of intense international traffic with limited control capacity)

**Criterion IV — Significant risk of international travel or trade restrictions.**
- Have similar past events resulted in international restrictions?
- Is the suspected/known source a traded food product, water, or other internationally traded good?
- Is the event associated with an international gathering or area of intense tourism?
- Is there foreign-official or international-media interest?

## 3. Applying it — key judgment calls

- **Criteria are situational, not mechanical.** The same disease can code differently depending on place, time, population, and context — this isn't a lookup table. A large endemic outbreak with no unusual features and no international link can fail to meet even one criterion; a single unusual case with international-gathering exposure can meet three.
- **Reassess as new information arrives.** An initially negative assessment can become notifiable with new information (e.g., international media attention emerging later changes Criterion IV).
- **Consultation is a real middle option (Article 8).** When information is insufficient to complete the assessment, or the event doesn't meet notification criteria but the jurisdiction still wants WHO input, consulting WHO is available and distinct from formal notification.
- **A "yes" on notification obligation is not the same as a PHEIC.** Formal notification opens a dialogue with WHO; only a small fraction of notified events are ultimately determined to be a Public Health Emergency of International Concern.

## 4. Brief illustrative examples (condensed and paraphrased from WHO's own case-scenario library)

- A recurring, seasonal cholera outbreak confined to one remote area, with a known source and no international travel link, met only one of the four criteria (impact) and was **not** notifiable — despite being serious locally.
- The same pathogen in a different context — a cluster of cholera cases among international tourists at a resort, with confirmed onward spread to a second country — met three criteria (unusual, international spread, and trade/travel risk) and **was** notifiable.
- A single laboratory-acquired case of cutaneous anthrax with a fully traced source and no further spread risk met only one criterion and was **not** notifiable, despite anthrax's high-consequence reputation.

This pattern — the same hazard resolving differently depending on context — is the central design idea of Annex 2, and mirrors why QIRA's own Domain 1 override (documenting a reason to walk the full tree even for a listed high-threat hazard) exists for the same reason.

## 5. How this integrates with the QIRA walk

At Step 11 (footnote (i)):
1. If the hazard is one of the four Category A diseases (§1), notification is already required regardless of the QIRA risk level — state this plainly, don't run the four-criteria assessment.
2. Otherwise, run the four criteria in §2 against the signal's own facts (not against the QIRA risk level) and report how many are met.
3. Note explicitly that this determination is independent of the QIRA terminal risk level — a QIRA "Low" and an Annex 2 notification obligation can coexist, and vice versa.
