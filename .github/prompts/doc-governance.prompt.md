---
mode: edit
---

# Doc ガバナンス統制プロンプト

目的: 既存ドキュメント全体の整合性 / 欠落 / 重複を自動点検しレポート生成

## 入力

- scanMode: incremental | full
- 変更差分 (optional)
- 対象日時 / ブランチ
- 除外パス (任意)

## 手順

1. ファイル列挙 → 種別分類
2. テンプレ必須節チェック
3. 参照解決 (相互リンク / 孤立検出)
4. ADR Status 整合性と Superseded 連鎖検査
5. 未決事項集約 → チケット化提案
6. インデックス更新ドラフト生成
7. レポート出力 + コミットメッセージ案

## 出力

Sections: Summary / Stats / Violations / Orphans / MissingSections / ADRGraph / OpenQuestions / Actions / CommitMessage

不足情報は質問列挙。推測禁止。
