# vns-doc-generator クイックスタートガイド

## はじめに
このガイドでは、`vns-doc-generator` chatmodeを使用して、vns-masakinihirotaプロジェクトのドキュメントを自動生成する方法を説明します。

---

## 前提条件

### 1. chatmodeの配置
以下のファイルが正しく配置されていることを確認:
```
vns-masakinihirota/.github/chatmodes/vns-doc-generator.chatmode.md
```

### 2. VitePressのセットアップ
vns-masakinihirota-docでVitePressがセットアップされていること。
未セットアップの場合は [VitePress セットアップガイド](./vitepress-setup.md) を参照。

---

## 基本的な使い方

### ステップ1: chatmodeの起動

1. VS Codeで GitHub Copilot Chatを開く
2. chatmode選択から `vns-doc-generator` を選択
3. 以下のようなプロンプトを入力:

```
作品登録機能の利用者向けドキュメントを生成してください
```

### ステップ2: 必須項目の確認

AIが以下の質問をします（最小限の質問のみ）:

```
Q1: ドキュメント種別
A. 利用者向けドキュメント

Q2: 対象機能
作品登録

Q3: 出力先ファイルパス（省略可）
docs/user-guide/works.md
```

確認して「はい」または「OK」と返答。

### ステップ3: 自動生成

AIが以下を自動実行:
1. Serena MCPでプロジェクト構造を把握
2. 関連コード（コンポーネント、Server Actions等）を収集
3. ドキュメントを生成
4. 生成内容を表示

### ステップ4: 確認と出力

生成されたドキュメントを確認し、問題なければ:
```
出力してください
```

これで実際にファイルが作成されます。

---

## プロンプトの例

### 利用者向けドキュメント

#### 例1: 新機能のドキュメント生成
```
プロフィール管理機能の利用者向けドキュメントを生成してください
```

#### 例2: 既存ドキュメントの更新
```
docs/user-guide/matching.md を最新のコードに基づいて更新してください
```

#### 例3: 複数機能のバッチ生成
```
以下の機能の利用者向けドキュメントを生成してください:
- 作品登録
- リスト機能
- タグ機能
```

### 開発者向けドキュメント

#### 例1: コンポーネントAPI仕様
```
プロフィール管理機能の開発者向けドキュメントを生成してください
コンポーネントのProps定義とServer Actionsを含めてください
```

#### 例2: データベーススキーマ
```
作品管理に関連するデータベーススキーマのドキュメントを生成してください
出力先: docs/developer-guide/database-works.md
```

#### 例3: API仕様書
```
作品登録のAPI仕様書を生成してください
Server Actionsとエンドポイントを含めてください
```

---

## 生成されるドキュメントの構成

### 利用者向けドキュメント
```markdown
---
title: 作品登録
description: 作品を登録・管理する機能
---

# 作品登録

## 概要
（機能の目的と特徴）

## 主要機能
- 作品情報の登録
- 評価システム
- カテゴリ分類

## 使い方
### ステップ1: 作品情報の入力
（詳細な手順）

### ステップ2: カテゴリの選択
（詳細な手順）

## よくある質問
### Q: 作品を削除できますか？
A: はい、...

## 関連ページ
- [作品評価](./works-rating.md)
- [リスト機能](./lists.md)
```

### 開発者向けドキュメント
```markdown
---
title: 作品登録 - 開発者ガイド
description: 作品登録機能の実装仕様
---

# 作品登録 - 開発者ガイド

## アーキテクチャ
（コンポーネント構成図）

## コンポーネントAPI

### WorkRegistrationForm
```typescript
interface WorkRegistrationFormProps {
  onSubmit: (data: WorkFormData) => Promise<void>;
  initialData?: WorkFormData;
}
```

## Server Actions

### createWork
```typescript
async function createWork(formData: FormData): Promise<Result<Work>>
```

## データベーススキーマ

### works テーブル
（テーブル定義）

## 実装例
（コードサンプル）

## 関連ファイル
- `src/app/(public)/works/page.tsx`
- `src/components/works/work-registration-form.tsx`
```

---

## Tips

### 効率的な活用方法

1. **機能単位で生成**: 大きな機能は分割して生成
   ```
   まず「作品登録の基本機能」のドキュメントを生成し、
   次に「作品評価機能」を別途生成
   ```

2. **既存ドキュメントの段階的更新**: 一度に全部更新せず、変更箇所のみ
   ```
   docs/user-guide/profile.md の「千の仮面システム」セクションを更新してください
   ```

3. **設計書との差異チェック**: 実装と設計書の乖離を検出
   ```
   作品登録機能について、設計書と実装の差異をチェックして、
   ドキュメントに反映してください
   ```

### よくあるユースケース

#### ユースケース1: 新機能リリース前
```
1. 実装完了
2. chatmodeでユーザーガイドを自動生成
3. 内容確認・修正
4. デプロイと同時にドキュメント公開
```

#### ユースケース2: リファクタリング後
```
1. コンポーネントを整理
2. chatmodeで開発者ドキュメントを更新
3. Props定義やAPI仕様が最新に
```

#### ユースケース3: バグ修正
```
1. バグ修正（動作変更あり）
2. chatmodeで該当機能のユーザーガイドを更新
3. 「修正内容」セクションを追加
```

---

## トラブルシューティング

### Q: chatmodeが見つからない
A: `.github/chatmodes/` に正しく配置されているか確認してください。

### Q: コード分析に時間がかかる
A: 対象機能を具体的に絞り込んでください。例: 「作品登録の基本機能のみ」

### Q: 生成されたドキュメントが不正確
A: 以下を確認:
- 対象機能の指定が正しいか
- 最新のコードがコミットされているか
- 設計書との整合性（必要に応じて参照）

### Q: VitePressでリンクが切れる
A: 相対パスを確認。chatmodeは自動で相対パスを生成しますが、
   ディレクトリ構造が変わった場合は手動修正が必要です。

---

## 次のステップ

### 1. VitePressサイトの確認
```bash
cd vns-masakinihirota-doc
pnpm docs:dev
```

### 2. ドキュメントのレビュー
生成されたドキュメントを確認し、必要に応じて修正。

### 3. デプロイ
```bash
pnpm docs:build
```

### 4. 継続的な更新
コード変更時は、該当機能のドキュメントも更新。

---

## サポート

### 質問・問題報告
- GitHub Issues: [vns-masakinihirota-doc](https://github.com/masakinihirota/vns-masakinihirota-doc)
- 設計書参照: [vns-masakinihirota-design](https://github.com/masakinihirota/vns-masakinihirota-design)

### 関連ドキュメント
- [VitePress セットアップガイド](./vitepress-setup.md)
- [プロジェクト README](../../README.md)
- [用語集](../../用語.md)
