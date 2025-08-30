# API概要

## 1. masakinihirota API について

**masakinihirota API** は、価値観共有プラットフォームの機能を外部アプリケーションから利用するためのRESTful APIです。

### 1.1 API の設計思想
- **RESTful設計**: HTTP標準に準拠した設計
- **JSON形式**: データ交換はJSON形式で統一
- **セキュリティ重視**: 厳格な認証・認可システム
- **レート制限**: 適切な利用制限による安定性確保

### 1.2 対応機能
現在のAPIでは以下の機能を提供しています：
- ユーザー認証・管理
- プロフィール管理（千の仮面システム）
- 作品登録・評価システム
- マッチング機能
- リスト管理機能
- タグ管理機能

## 2. API 基本情報

### 2.1 ベースURL
```
https://api.masakinihirota.com/v1
```

### 2.2 リクエスト形式
- **Content-Type**: `application/json`
- **文字エンコーディング**: UTF-8
- **HTTPメソッド**: GET, POST, PUT, DELETE

### 2.3 レスポンス形式
すべてのAPIレスポンスは以下の基本構造を持ちます：

```json
{
  "success": true,
  "data": {
    // レスポンスデータ
  },
  "message": "操作が正常に完了しました",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

エラー時のレスポンス：
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "入力データが無効です",
    "details": {
      // エラー詳細
    }
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

## 3. 認証システム

### 3.1 OAuth 2.0認証
外部アプリケーションからの利用には、OAuth 2.0による認証が必要です。

対応プロバイダー：
- Google
- GitHub
- その他（順次拡大予定）

### 3.2 APIキー認証
開発者向けには、APIキーによる認証も提供しています。

## 4. レート制限

### 4.1 制限内容
- **一般利用**: 1時間あたり1000リクエスト
- **認証済み**: 1時間あたり5000リクエスト
- **プレミアム**: 1時間あたり10000リクエスト

### 4.2 制限超過時の処理
制限を超えた場合、HTTP 429 (Too Many Requests) を返します。

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "API制限を超えました",
    "retry_after": 3600
  }
}
```

## 5. エラーハンドリング

### 5.1 HTTPステータスコード
- `200 OK`: 成功
- `201 Created`: リソース作成成功
- `400 Bad Request`: リクエストエラー
- `401 Unauthorized`: 認証エラー
- `403 Forbidden`: 権限エラー
- `404 Not Found`: リソースが見つからない
- `429 Too Many Requests`: レート制限超過
- `500 Internal Server Error`: サーバーエラー

### 5.2 エラーコード
| コード | 説明 | 対処方法 |
|--------|------|----------|
| `VALIDATION_ERROR` | 入力データエラー | リクエストデータを確認 |
| `AUTHENTICATION_FAILED` | 認証失敗 | 認証情報を確認 |
| `PERMISSION_DENIED` | 権限不足 | 必要な権限を確認 |
| `RESOURCE_NOT_FOUND` | リソース未発見 | リソースの存在を確認 |
| `RATE_LIMIT_EXCEEDED` | レート制限超過 | 時間をおいて再試行 |

## 6. バージョニング

### 6.1 APIバージョン管理
- **現在バージョン**: v1
- **バージョン指定**: URLパスで指定 (`/v1/`)
- **下位互換性**: メジャーバージョン内で保証

### 6.2 廃止予定機能
廃止予定の機能については、事前に通知し、十分な移行期間を設けます。

## 7. SDKとライブラリ

### 7.1 公式SDK
現在、以下の言語向けSDKを提供予定：
- JavaScript/TypeScript
- Python
- Go
- PHP

### 7.2 コミュニティライブラリ
コミュニティによる非公式ライブラリも順次公開予定です。

## 8. 開発者サポート

### 8.1 ドキュメント
- [認証ガイド](./authentication.md)
- [エンドポイント一覧](./endpoints.md)
- [コード例集](./examples.md)

### 8.2 サポート
- **開発者コミュニティ**: Discord
- **技術サポート**: メール
- **バグレポート**: GitHub Issues

## 9. 利用規約

### 9.1 使用制限
- 商用利用は別途契約が必要
- データスクレイピングは禁止
- プラットフォームの安定性を損なう行為は禁止

### 9.2 データ利用
- ユーザーデータの適切な取り扱いが必要
- プライバシーポリシーの遵守が必要
- データの第三者提供には制限あり

## 10. 更新情報

APIの更新情報は以下で確認できます：
- [更新ログ](./changelog.md)
- [開発者ブログ](https://blog.masakinihirota.com/api)
- [メーリングリスト](https://newsletter.masakinihirota.com)

## 11. クイックスタート

### 11.1 基本的な使用例
```javascript
// 認証
const auth = await authenticate('your-api-key');

// ユーザー情報取得
const user = await api.users.me();

// 作品検索
const works = await api.works.search({
  genre: 'anime',
  tags: ['SF', '価値観']
});
```

詳細な使用方法については、[エンドポイント一覧](./endpoints.md)をご確認ください。
