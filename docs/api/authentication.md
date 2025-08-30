# API認証

## 1. 認証方式の概要

**masakinihirota API** では、セキュリティを重視した複数の認証方式を提供しています。用途に応じて最適な認証方式をお選びください。

## 2. OAuth 2.0 認証

### 2.1 OAuth 2.0 とは
OAuth 2.0は、第三者アプリケーションがユーザーの許可を得て、限定的にAPIへアクセスできる仕組みです。

### 2.2 対応プロバイダー
- **Google**: Google アカウントでの認証
- **GitHub**: GitHub アカウントでの認証
- **Discord**: Discord アカウントでの認証（予定）
- **Twitter**: Twitter アカウントでの認証（予定）

### 2.3 OAuth 2.0 フロー

#### Step 1: 認証URL生成
```http
GET https://auth.masakinihirota.com/oauth/authorize
```

パラメータ：
```
?response_type=code
&client_id=YOUR_CLIENT_ID
&redirect_uri=YOUR_REDIRECT_URI
&scope=profile,works:read,lists:write
&state=RANDOM_STATE_STRING
```

#### Step 2: ユーザー認証
ユーザーが認証プロバイダーで認証を行い、あなたのアプリケーションへの権限付与を承認します。

#### Step 3: 認証コード取得
```
https://your-app.com/callback?code=AUTHORIZATION_CODE&state=STATE_STRING
```

#### Step 4: アクセストークン取得
```http
POST https://auth.masakinihirota.com/oauth/token
Content-Type: application/json

{
  "grant_type": "authorization_code",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "code": "AUTHORIZATION_CODE",
  "redirect_uri": "YOUR_REDIRECT_URI"
}
```

レスポンス：
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "scope": "profile works:read lists:write"
}
```

### 2.4 アクセストークン使用
```http
GET https://api.masakinihirota.com/v1/users/me
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 2.5 トークンリフレッシュ
```http
POST https://auth.masakinihirota.com/oauth/token
Content-Type: application/json

{
  "grant_type": "refresh_token",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "refresh_token": "YOUR_REFRESH_TOKEN"
}
```

## 3. APIキー認証

### 3.1 APIキーとは
開発者向けに提供される、シンプルで直接的な認証方式です。

### 3.2 APIキー取得方法
1. [開発者ポータル](https://developer.masakinihirota.com) にログイン
2. 新しいアプリケーションを作成
3. APIキーを生成・取得

### 3.3 APIキー使用方法

#### ヘッダー認証（推奨）
```http
GET https://api.masakinihirota.com/v1/works
X-API-Key: YOUR_API_KEY
```

#### クエリパラメータ認証
```http
GET https://api.masakinihirota.com/v1/works?api_key=YOUR_API_KEY
```

**注意**: セキュリティ上の理由から、ヘッダー認証を推奨します。

## 4. スコープ（権限）

### 4.1 利用可能なスコープ
| スコープ | 説明 | 主な操作 |
|---------|------|----------|
| `profile` | プロフィール情報 | 基本情報の読み取り |
| `profile:write` | プロフィール編集 | プロフィール情報の更新 |
| `works:read` | 作品情報読み取り | 作品データの参照 |
| `works:write` | 作品情報更新 | 作品登録・評価 |
| `lists:read` | リスト読み取り | リスト情報の参照 |
| `lists:write` | リスト編集 | リスト作成・更新 |
| `matching:read` | マッチング情報 | マッチング結果の参照 |
| `admin` | 管理者権限 | システム管理操作 |

### 4.2 スコープの指定
OAuth認証時にスコープを指定：
```
scope=profile+works:read+lists:write
```

複数スコープはプラス（+）または空白文字で区切ります。

## 5. セキュリティベストプラクティス

### 5.1 トークン管理
- **安全な保存**: トークンは安全な場所に保存
- **定期的な更新**: refresh tokenを使用した定期更新
- **適切な権限**: 必要最小限のスコープのみ要求
- **有効期限の確認**: トークンの有効期限を定期チェック

### 5.2 APIキー管理
- **環境変数使用**: APIキーは環境変数で管理
- **定期的なローテーション**: APIキーの定期的な更新
- **権限制限**: 必要最小限の権限のみ付与
- **アクセスログ監視**: 不正なアクセスの監視

### 5.3 通信セキュリティ
- **HTTPS必須**: すべての通信でHTTPS使用
- **証明書検証**: SSL証明書の適切な検証
- **リクエスト検証**: リクエストの改ざん検出

## 6. 認証エラー

### 6.1 一般的なエラー
| エラーコード | HTTPステータス | 説明 |
|-------------|---------------|------|
| `INVALID_TOKEN` | 401 | トークンが無効または期限切れ |
| `INSUFFICIENT_SCOPE` | 403 | 必要なスコープが不足 |
| `INVALID_API_KEY` | 401 | APIキーが無効 |
| `TOKEN_EXPIRED` | 401 | アクセストークンが期限切れ |
| `INVALID_GRANT` | 400 | 認証グラント（コード）が無効 |

### 6.2 エラー例
```json
{
  "success": false,
  "error": {
    "code": "INVALID_TOKEN",
    "message": "提供されたトークンが無効です",
    "details": {
      "reason": "token_expired",
      "expires_at": "2024-01-01T12:00:00Z"
    }
  },
  "timestamp": "2024-01-01T12:05:00Z"
}
```

## 7. 実装例

### 7.1 JavaScript/Node.js
```javascript
// OAuth認証
const authUrl = 'https://auth.masakinihirota.com/oauth/authorize?' +
  new URLSearchParams({
    response_type: 'code',
    client_id: process.env.CLIENT_ID,
    redirect_uri: 'http://localhost:3000/callback',
    scope: 'profile works:read',
    state: generateState()
  });

// APIキー認証
const response = await fetch('https://api.masakinihirota.com/v1/users/me', {
  headers: {
    'X-API-Key': process.env.API_KEY,
    'Content-Type': 'application/json'
  }
});
```

### 7.2 Python
```python
import requests
import os

# APIキー認証
headers = {
    'X-API-Key': os.getenv('API_KEY'),
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://api.masakinihirota.com/v1/users/me',
    headers=headers
)
```

## 8. 開発者ツール

### 8.1 認証テスター
開発者ポータルで認証フローをテストできるツールを提供しています。

### 8.2 デバッグ情報
認証エラー時に詳細なデバッグ情報を提供します（開発環境のみ）。

## 9. FAQ

### Q: リフレッシュトークンの有効期限は？
A: リフレッシュトークンは90日間有効です。定期的に使用することで自動更新されます。

### Q: APIキーは何個まで作成できる？
A: 1つのアプリケーションにつき、最大5個まで作成可能です。

### Q: 本番環境でのセキュリティ推奨事項は？
A: HTTPS必須、適切なスコープ設定、定期的なキーローテーション、アクセスログの監視を推奨します。

## 10. サポート

認証に関する問題については：
- [開発者ドキュメント](https://docs.masakinihirota.com)
- [サポートフォーラム](https://community.masakinihirota.com)
- [技術サポート](mailto:dev-support@masakinihirota.com)
