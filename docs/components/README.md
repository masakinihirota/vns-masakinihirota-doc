# コンポーネント設計ガイド

## 分類
| 種別 | 目的 |
|------|------|
| Presentational | UI 表示のみ |
| Container | Server Action 呼び出し・状態集約 |
| Form | Conform + Zod バリデーション |

## 命名
- ディレクトリ: kebab-case
- コンポーネント: PascalCase
- エクスポート: 名前付き export

## Props ドキュメント テンプレ
| Prop | 型 | 必須 | 説明 | 既定 |
|------|----|------|------|------|

## アクセシビリティ最小要件
- role 適切化 (button, dialog 等)
- フォーカスリング非除去
- aria-* 自動/必要明示

## アニメーション指針
| イベント | エフェクト |
|----------|------------|
| mount | fadeIn + slideDown (300ms) |
| unmount | fadeOut + slideUp (200ms) |
| complete | scaleIn + colorChange (150ms) |

## 状態管理
- 単純: 内部 useState
- 跨コンポーネント: Zustand store
- 一時フォーム: Conform state

## テスト
- 単一責務: 1 動作 1 テスト
- a11y: キーボード操作 / aria-assertions

## 未決
- Storybook 自動 snapshot 導入方式
- デザイントークン抽出自動化

