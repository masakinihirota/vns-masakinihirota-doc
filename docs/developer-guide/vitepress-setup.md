# VitePress ドキュメントサイト セットアップガイド

## 概要
このガイドでは、vns-masakinihirota-docリポジトリでVitePressを使用したドキュメントサイトのセットアップ方法を説明します。

## 前提条件
- Node.js 18.0以上
- pnpm 9.0以上

## セットアップ手順

### 1. VitePressのインストール

```bash
cd vns-masakinihirota-doc

# package.jsonがない場合
pnpm init

# VitePressをインストール
pnpm add -D vitepress
```

### 2. package.jsonのscripts追加

```json
{
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  }
}
```

### 3. ディレクトリ構造の確認

```
vns-masakinihirota-doc/
├── .vitepress/
│   └── config.ts          # VitePress設定ファイル（既に作成済み）
├── docs/
│   ├── index.md           # トップページ
│   ├── user-guide/        # ユーザーガイド
│   │   ├── getting-started.md
│   │   ├── account.md
│   │   ├── profile.md
│   │   ├── works.md
│   │   ├── matching.md
│   │   ├── lists.md
│   │   └── tags.md
│   ├── developer-guide/   # 開発者ガイド（新規作成）
│   │   ├── overview.md
│   │   ├── setup.md
│   │   ├── architecture.md
│   │   └── database-schema.md
│   ├── api/              # API リファレンス
│   │   ├── overview.md
│   │   ├── authentication.md
│   │   └── endpoints.md
│   └── faq.md
├── package.json
└── README.md
```

### 4. index.md（トップページ）の作成

`docs/index.md` を以下の内容で作成:

```markdown
---
layout: home

hero:
  name: "masakinihirota"
  text: "価値観共有プラットフォーム"
  tagline: オアシス宣言・人間宣言のもと、安心で安全なオンライン空間を提供します
  actions:
    - theme: brand
      text: ユーザーガイド
      link: /user-guide/getting-started
    - theme: alt
      text: 開発者ガイド
      link: /developer-guide/overview

features:
  - icon: 🎭
    title: 千の仮面システム
    details: 複数のペルソナを管理し、状況に応じて使い分けることができます
  - icon: 📊
    title: 絶対相対評価
    details: 客観的で公正な作品評価システムを提供します
  - icon: 🤝
    title: 価値観マッチング
    details: 価値観に基づいた質の高いつながりを実現します
  - icon: 🏷️
    title: タグ・リスト機能
    details: 公式タグとユーザータグで作品を効率的に管理できます
---
```

### 5. 開発者ガイドの初期ページ作成

`docs/developer-guide/overview.md`:

```markdown
---
title: 開発者ガイド - 概要
description: vns-masakinihirotaの開発者向けドキュメント
---

# 開発者ガイド

## 概要
vns-masakinihirotaは、Next.js 15とSupabaseをベースにした価値観共有プラットフォームです。

## 技術スタック
- **フロントエンド**: Next.js 15, React 19, TypeScript
- **UIライブラリ**: shadcn/ui, Tailwind CSS
- **バックエンド**: Supabase (Auth, Database, Realtime)
- **ORM**: Drizzle ORM
- **国際化**: next-intl（日本語、英語、ドイツ語）

## 主要機能
- ユーザー認証（Google, GitHub, 匿名）
- プロフィール管理（千の仮面システム）
- 作品登録・評価（絶対相対評価）
- 価値観マッチング
- リスト・タグ管理

## 次のステップ
- [環境構築](./setup.md)
- [アーキテクチャ](./architecture.md)
- [データベーススキーマ](./database-schema.md)
```

### 6. 開発サーバーの起動

```bash
pnpm docs:dev
```

ブラウザで `http://localhost:5173` にアクセスして確認。

### 7. 本番ビルド

```bash
pnpm docs:build
pnpm docs:preview
```

### 8. デプロイ（例: GitHub Pages）

`.github/workflows/deploy.yml` を作成:

```yaml
name: Deploy VitePress

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v3
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install

      - name: Build
        run: pnpm docs:build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/.vitepress/dist
```

## ドキュメント自動生成の使い方

### chatmodeの実行

1. VS Codeで `vns-doc-generator` chatmodeを選択
2. プロンプト例:
   ```
   作品登録機能の利用者向けドキュメントを生成してください
   ```
3. AIが必須項目を質問
4. 確認後、ドキュメントが自動生成される

### 手動での更新

既存ドキュメントを手動更新する場合:
```
docs/user-guide/works.md を最新のコードに基づいて更新してください
```

## トラブルシューティング

### ビルドエラー
- `node_modules` と `.vitepress/cache` を削除して再インストール
  ```bash
  rm -rf node_modules .vitepress/cache
  pnpm install
  ```

### リンク切れ
- 相対パスが正しいか確認
- `.md` 拡張子を省略しない（VitePressは自動で処理）

### 日本語検索が機能しない
- `config.ts` の `search` 設定を確認
- ローカル検索は標準で日本語対応

## 参考資料
- [VitePress公式ドキュメント](https://vitepress.dev/)
- [VitePress日本語ガイド](https://vitepress.dev/ja/)
- [プロジェクトREADME](../README.md)
