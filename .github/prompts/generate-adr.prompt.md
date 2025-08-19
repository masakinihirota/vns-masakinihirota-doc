---
mode: edit
---

# ADR 生成プロンプト

## 入力

- contextSummary
- decisionDrivers
- consideredOptions[]
- selectedOption
- consequences 期待
- relatedSpecs / commits

## 出力

(ADR-<連番>-<kebab>.md)

```
# ADR-<n>-<name>
Status: Proposed
Date: YYYY-MM-DD
## Context
## Drivers
## Options
## Decision
## Rationale
## Consequences (+ / -)
## Alternatives Rejected
## Follow-up
## Links
```

不足 → 質問列挙。連番重複禁止 (既存走査)。
