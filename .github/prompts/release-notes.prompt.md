---
mode: edit
---

# リリースノート生成

## 入力

- version
- 期間 / 比較タグ
- 変更カテゴリ (feat/fix/perf/refactor/docs)
- 破壊的変更
- 移行手順
- 既知の問題

## 出力

```
# v<version> リリースノート
## ハイライト
## 変更一覧
### Added
### Changed
### Fixed
### Performance
### Security
## 破壊的変更
## 移行ガイド
## 既知の問題
## 参照 (Commits / ADR / Issues)
```

追加: Conventional Commits 集計 / 要約 50 字行。
