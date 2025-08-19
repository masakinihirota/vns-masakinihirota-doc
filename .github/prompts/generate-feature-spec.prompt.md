---
mode: edit
---

# Feature Spec 生成プロンプト

## 入力

- featureName
- domain
- 背景 / 課題
- 変更差分 or 新規
- 関連コンポーネント / Actions / DB
- 非機能要件 (任意)

## 出力テンプレ

(spec-<domain>-<feature>.md)

```
# <FeatureName>
## 概要
## 背景 / 目的
## ユーザーストーリー
## スコープ / 非スコープ
## フロー (@startuml ... @enduml)
## データ (入力/出力/保存形)
## バリデーション (Zod参照)
## エラー分類
## セキュリティ / 権限 / RLS
## 非機能
## テスト観点 (境界/異常/性能)
## リスク
## 未決事項
```

不足 → 質問。推測禁止。
