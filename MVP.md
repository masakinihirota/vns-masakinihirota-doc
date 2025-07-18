# MVPタスク一覧

## 1. 認証・認可
- OAuth認証(Google, GitHub)によるユーザー登録・ログイン
- 匿名認証対応
- 認証なしダミープロフィール閲覧機能

## 2. ルートアカウント管理
- 認証後のルートアカウント自動生成 (UUID v4)
- ルートアカウント基本情報入力フォーム（居住地域・母語・世代等）
- RLS設定による権限制御の初期構築

## 3. ユーザープロフィール
- プロフィール新規作成・編集画面
- 複数プロフィール作成 (千の仮面)
- プロフィール一覧／詳細閲覧

## 4. 登録機能
- 作品登録フォーム (タイトル、カテゴリ、タグ、URL)
- 価値観選択機能 (基本お題)
- リスト／チェーンの登録・一覧表示

## 5. マッチング
- 自動マッチングアルゴリズム (Tier1~3の共通作品数)
- マッチング結果一覧画面
- ウォッチ／フォローボタン実装

## 6. UI・ナビゲーション
- Next.js App Router ベースのページ構成
- 上部ナビゲーション + 左サイドメニューの骨格
- ダークモード・言語切替トグル

## 7. インフラ・バックエンド
- Supabase Auth／Database初期セットアップ
- Zodを用いた入力バリデーション

## 8. テスト
- 単体テスト環境構築(Vitest, React Testing Library)
- E2Eテスト雛形(Playwright/Cypress)
- GitHub Actions連携による自動実行
