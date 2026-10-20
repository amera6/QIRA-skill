# QIRA — Risk Classification, Immediate Actions, and Footnotes

**Companion to**: `qira-assessor` SKILL.md.

**Source**: *QIRA User Manual*, §3.3–3.5, §4.1.

Read this file at Step 9 (risk level is already determined via `domains_and_questions.md` §6 by this point) and Step 11 (selecting immediate actions).

---

## 1. The five risk levels

QIRA resolves to exactly one of: **Very low, Low, Moderate, High, Very high.** The level is a *terminal output* of the routing table — there's no separate scoring or averaging step; whichever terminal node the walk lands on **is** the risk level.

## 2. Predefined immediate actions

Immediate actions are meant to be **predefined per risk level by the Member State or subnational entity in advance**, not invented fresh for each assessment. If the analyst's context has no such predefined list, treat the following as an illustrative starting menu (not a template to fill mechanically) and flag in the Results Recording Form that the Member State should formalize its own list for future use:

- Informing top management in the health structure.
- Deploying rapid response teams to the affected area.
- Considering activation of the emergency response plan (national or subnational level).
- Providing support — enhanced surveillance, laboratory testing, epidemiological investigation, clinical management, and supplying materials, diagnostics, vaccines, therapeutics.
- Monitoring the signal/event through routine surveillance.
- Sharing information with neighbouring provinces/regions, relevant offices, and colleagues.
- Performing a more comprehensive, multidisciplinary rapid risk assessment.
- Discarding the signal/event (appropriate at Very low, when Domain 4.1 resolves NO with no further questions).

This list is neither comprehensive nor prescriptive — add or substitute actions to fit the nature and context of the specific signal or event.

## 3. Footnotes — considerations that apply regardless of risk level

These sit outside the branching logic and should be checked every time, not just at specific risk levels:

**(i) IHR (2005) Annex 2.** Always run an IHR Annex 2 notification check (as amended by WHA77.17) for any event that may meet notification criteria. Use `references/ihr_annex2_decision_instrument.md` for the actual four-criteria instrument and disease lists rather than reasoning from general knowledge — this determination is independent of the QIRA risk level, and never treat a low QIRA result as grounds to skip it.

**(ii) International spread risk.** If there's a risk of the event spreading across borders, share information promptly with neighbouring countries/areas, and encourage them to assess their own importation risk.

**(iii) Public concern / political sensitivity.** High public concern or political sensitivity may itself warrant faster information release, more intensive risk communication, and higher-level management engagement — independent of the risk level the algorithm produced.

**(iv) No predefined high-threat list, or hazard not on it.** Proceed through the domains in the logical flow, following the "no/unknown" pathway from Domain 1.

**(v) Novel or unknown hazard.** The team decides, as a judgement call, whether to route Domain 1 as YES or NO/UNKNOWN for a hazard that's genuinely novel or unclassified. Document the reasoning either way.

## 4. When QIRA alone isn't enough

A Moderate, High, or Very high result — or an event with serious potential implications, IHR Annex 2 relevance, multi-jurisdiction spread, or unknown aetiology — is a signal that a more comprehensive, multidisciplinary rapid risk assessment process may be warranted beyond what QIRA's fixed yes/no/unknown format can capture (see `algorithm_essentials.md` §6.1). Flag this in the output per Step 11 of SKILL.md, without prescribing which specific downstream tool or process the jurisdiction should use for that follow-up — that's a local decision outside QIRA's own scope.
