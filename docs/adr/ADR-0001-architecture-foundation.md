# ADR-0001-architecture-foundation
Status: Proposed
Date: 2025-08-19

## Context
MVP フェーズで迅速かつ型安全な開発を行う基盤選定が必要。SSR/クライアント混在、フォーム検証、DB アクセス、RLS。

## Decision
Next.js App Router + Server Actions + Supabase (Auth/DB/Storage) + Drizzle ORM + Zod + Conform + Tailwind + Radix UI/Shadcn + Zustand を標準採用。

## Drivers
- 型安全 (Zod + Drizzle)
- RLS によるデータ境界
- Server Actions による API レイヤ軽量化
- 再利用可能な UI トークン

## Alternatives
| 案 | 却下理由 |
|----|----------|
| Prisma + REST | RLS 組込負荷 / Server Actions 利点減 |
| TRPC 導入 | 初期複雑性上昇 (MVP 過剰) |
| Formik | Conform の progressive enhancement / 型強制優位 |

## Consequences
+ コード量削減 (API boilerplate)
+ RLS で最小権限
- Supabase ベンダーロック度増
- Server Actions 監視/ロギング工夫必要

## Rationale
高速プロトタイピングと保守性のバランス。脱線を防ぎドメインロジック集中。

## Follow-up
- ログ基盤 (Sentry + structured logs)
- パフォーマンス計測 (Web Vitals / Supabase EXPLAIN)
- Server Action 規約ドキュメント化 (命名 / 返却型)

## Links
- specs/spec-core-platform.md

