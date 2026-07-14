# QIRA Assessor — Claude Skill

A Claude skill implementing the WHO Quick and Immediate Risk Assessment (QIRA) algorithm: a fast, hierarchical yes/no/unknown decision tree across five domains (high-threat hazard, exposure, severity, spread/scale, capacity) that resolves any acute public health signal or event to a risk level (Very low → Very high) plus predefined immediate actions.

General-purpose and self-contained — not tied to any specific program, bulletin, or other assessment framework.

## What's inside

```
qira-assessor/
├── SKILL.md                          # Core procedure (14 steps, 3 modes)
├── references/
│   ├── algorithm_essentials.md       # What QIRA is, scope-setting, confidence, limitations
│   ├── domains_and_questions.md      # The five domains + full routing logic
│   ├── risk_classification_and_actions.md
│   ├── recording_form_template.md    # Field-by-field output guidance
│   └── worked_example.md
└── assets/
    ├── recording_form_blank.md       # Copy-ready output template
    └── qira_decision_tree.md         # Mermaid diagram of the routing logic
```

## Installing

1. Download this repo (or just the `qira-assessor` folder) as a ZIP, or clone it:
   ```bash
   git clone https://github.com/your-username/qira-assessor-skill.git
   ```
2. In Claude.ai: **Settings → Capabilities → Skills → Upload skill**, and select the `qira-assessor` folder (zipped).
3. In Claude Code: place the `qira-assessor` folder in your skills directory.

## Using it

Ask Claude something like:

> "Run a QIRA assessment on this signal: [paste a public health signal/outbreak description]"

Claude will confirm a mode (Autonomous / Hybrid / Interactive), walk the five domains, and produce a completed Results Recording Form.

## Testing status

Validated on 2026-07-10 against a 4-signal test battery covering four of the five distinct Question 5.2 capacity-gate branches (5.2a, 5.2b, 5.2d, 5.2e); gate 5.2c (reached via Q5.1 = No) has not yet been exercised. See `references/domains_and_questions.md` §6 for the full routing table.

## License

Add your preferred license here (e.g., MIT) if distributing further.
