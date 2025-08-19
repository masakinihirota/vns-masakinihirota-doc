---
mode: edit
---

# ドキュメント索引自動生成

## 入力

- scanPaths (既定: docs/)
- 対象種別フィルタ
- 直近変更閾値 (days)
- 出力パス (docs/index/overview.md)

## 出力構成

```
# Documentation Index
## 統計
## 種別別一覧
## ADR Status
## 最新変更 Top10
## 未決事項集約
## リンクマップ (簡易)
```

整合性警告を末尾に列挙（例: 欠落必須節 / 孤立文書）。
