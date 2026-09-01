<!--
QIRA decision-tree diagram, matching the corrected routing logic in
references/domains_and_questions.md §6. Render this Mermaid block directly
(GitHub, Obsidian, and most Markdown viewers with Mermaid support will do
so automatically) when a visual aid would help an analyst follow or explain
a walk, or embed it in a bulletin/report output.
-->

```mermaid
flowchart TD
    Q1["Domain 1 — Q1: High-threat hazard?"]
    Q2["Domain 2 — Q2: Further exposure likely?"]
    Q3["Domain 3 — Q3: Moderate–severe among cases?"]
    Q41["Q4.1: Significant number currently affected?"]
    Q42a["Q4.2: High future case count / spread? (via Q3=No)"]
    Q42b["Q4.2: High future case count / spread? (via Q3=Yes/Unknown)"]
    Q51["Q5.1: Health system likely overwhelmed?"]
    Q52a["Q5.2a: Capacities in place?"]
    Q52b["Q5.2b: Capacities in place?"]
    Q52c["Q5.2c: Capacities in place?"]
    Q52d["Q5.2d: Capacities in place?"]
    Q52e["Q5.2e: Capacities in place?"]

    VLow1(["Terminal: Very low"])
    VLow2(["Terminal: Very low"])
    Low1(["Terminal: Low"])
    Low2(["Terminal: Low"])
    Mod1(["Terminal: Moderate"])
    Mod2(["Terminal: Moderate"])
    High1(["Terminal: High"])
    High2(["Terminal: High"])
    VHigh1(["Terminal: Very high"])
    VHigh2(["Terminal: Very high"])

    Q1 -->|Yes, no override| Q52e
    Q1 -->|No / Unknown, or Yes+override| Q2

    Q2 -->|Yes / Unknown| Q3
    Q2 -->|No| Q41

    Q3 -->|No| Q42a
    Q3 -->|Yes / Unknown| Q42b

    Q41 -->|No| VLow1
    Q41 -->|Yes / Unknown| Q52a

    Q42a -->|No| Q52a
    Q42a -->|Yes / Unknown| Q52b

    Q42b -->|No| Q52b
    Q42b -->|Yes / Unknown| Q51

    Q51 -->|No| Q52c
    Q51 -->|Yes / Unknown| Q52d

    Q52a -->|Yes| VLow2
    Q52a -->|No / Unknown| Low1

    Q52b -->|Yes| Low2
    Q52b -->|No / Unknown| Mod1

    Q52c -->|Yes| Mod2
    Q52c -->|No / Unknown| High1

    Q52d -->|Yes| High2
    Q52d -->|No / Unknown| VHigh1

    Q52e -->|Yes| High2
    Q52e -->|No / Unknown| VHigh2
```

**Reading note**: Q5.2a through Q5.2e are the same *question* (Are capacities for prevention and control measures in place?) asked at five different points in the tree — the diagram deliberately draws them as separate nodes because each maps to a different terminal pair. This mirrors the fix applied to `references/domains_and_questions.md` §6 on 2026-07-10, after testing surfaced that an earlier version of this skill collapsed all five into one node.
