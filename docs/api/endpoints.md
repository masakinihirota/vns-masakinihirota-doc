# APIエンドポイント一覧

## 1. 認証・ユーザー管理

### 1.1 ユーザー情報
```http
GET /v1/users/me
```
現在認証されているユーザーの情報を取得

**必要なスコープ**: `profile`

**レスポンス例**:
```json
{
  "success": true,
  "data": {
    "id": "user_123",
    "email": "user@example.com",
    "created_at": "2024-01-01T00:00:00Z",
    "root_account": {
      "region": "asia",
      "languages": ["ja", "en"],
      "generation": "1990s"
    }
  }
}
```

### 1.2 プロフィール管理
```http
GET /v1/profiles
```
ユーザーの全プロフィール（千の仮面）を取得

**必要なスコープ**: `profile`

```http
POST /v1/profiles
```
新しいプロフィールを作成

**必要なスコープ**: `profile:write`

**リクエスト例**:
```json
{
  "name": "アニメ好きペルソナ",
  "description": "アニメとマンガ専用のプロフィール",
  "avatar_url": "https://example.com/avatar.png",
  "interests": ["anime", "manga", "SF"]
}
```

```http
PUT /v1/profiles/{profile_id}
```
指定したプロフィールを更新

```http
DELETE /v1/profiles/{profile_id}
```
指定したプロフィールを削除

## 2. 作品管理

### 2.1 作品検索・一覧
```http
GET /v1/works
```
作品一覧を取得

**クエリパラメータ**:
- `genre`: ジャンル
- `tags`: タグ（カンマ区切り）
- `year`: 公開年
- `limit`: 取得件数（デフォルト: 20, 最大: 100）
- `offset`: オフセット

**例**:
```http
GET /v1/works?genre=anime&tags=SF,価値観&limit=10
```

```http
GET /v1/works/{work_id}
```
指定した作品の詳細情報を取得

**必要なスコープ**: `works:read`

### 2.2 作品登録・更新
```http
POST /v1/works
```
新しい作品を登録

**必要なスコープ**: `works:write`

**リクエスト例**:
```json
{
  "title": "攻殻機動隊 STAND ALONE COMPLEX",
  "type": "anime",
  "genre": "SF",
  "year": 2002,
  "description": "近未来を舞台にした刑事アクションアニメ",
  "tags": ["SF", "哲学的", "サイバーパンク"],
  "creators": ["神山健治", "士郎正宗"]
}
```

```http
PUT /v1/works/{work_id}
```
指定した作品情報を更新

### 2.3 作品評価
```http
GET /v1/works/{work_id}/evaluations
```
指定した作品の評価一覧を取得

```http
POST /v1/works/{work_id}/evaluations
```
作品に評価を投稿

**リクエスト例**:
```json
{
  "score": 0,
  "comment": "私の基準作品です。価値観の描き方が素晴らしい。",
  "tags": ["価値観", "考察したくなる"],
  "profile_id": "profile_456"
}
```

```http
PUT /v1/evaluations/{evaluation_id}
```
自分の評価を更新

## 3. マッチング

### 3.1 マッチング結果取得
```http
GET /v1/matching/suggestions
```
おすすめユーザーを取得

**必要なスコープ**: `matching:read`

**クエリパラメータ**:
- `type`: マッチングタイプ（`value_based`, `work_based`, `interest_based`）
- `limit`: 取得件数

**レスポンス例**:
```json
{
  "success": true,
  "data": {
    "suggestions": [
      {
        "user_id": "user_789",
        "profile": {
          "name": "SF愛好家",
          "avatar_url": "https://example.com/avatar2.png"
        },
        "match_score": 0.85,
        "match_reasons": [
          "共通評価作品: 攻殻機動隊, Serial Experiments Lain",
          "類似価値観: 相互尊重, 探求心"
        ]
      }
    ]
  }
}
```

### 3.2 マッチング条件設定
```http
PUT /v1/matching/preferences
```
マッチング条件を設定

**リクエスト例**:
```json
{
  "age_range": [20, 40],
  "regions": ["asia", "europe"],
  "languages": ["ja", "en"],
  "value_priorities": ["相互尊重", "平和主義"],
  "interest_weight": 0.3,
  "value_weight": 0.7
}
```

## 4. リスト管理

### 4.1 リスト一覧・詳細
```http
GET /v1/lists
```
ユーザーのリスト一覧を取得

**必要なスコープ**: `lists:read`

```http
GET /v1/lists/{list_id}
```
指定したリストの詳細を取得

```http
GET /v1/lists/public
```
公開されているリストを取得

### 4.2 リスト作成・更新
```http
POST /v1/lists
```
新しいリストを作成

**必要なスコープ**: `lists:write`

**リクエスト例**:
```json
{
  "name": "価値観を考えさせるアニメ",
  "description": "深い価値観について考察できるアニメ作品集",
  "visibility": "public",
  "works": [
    {
      "work_id": "work_123",
      "order": 1,
      "comment": "最も価値観について考えさせられた作品"
    }
  ]
}
```

```http
PUT /v1/lists/{list_id}
```
指定したリストを更新

```http
DELETE /v1/lists/{list_id}
```
指定したリストを削除

### 4.3 リスト内作品管理
```http
POST /v1/lists/{list_id}/works
```
リストに作品を追加

```http
DELETE /v1/lists/{list_id}/works/{work_id}
```
リストから作品を削除

## 5. タグ管理

### 5.1 タグ一覧・検索
```http
GET /v1/tags
```
タグ一覧を取得

**クエリパラメータ**:
- `type`: タグタイプ（`official`, `user`, `all`）
- `category`: カテゴリ
- `search`: 検索キーワード
- `popular`: 人気順（`true`/`false`）

```http
GET /v1/tags/suggestions
```
入力補完用のタグ提案を取得

**クエリパラメータ**:
- `query`: 入力文字列
- `context`: コンテキスト（`work`, `profile`, `list`）

### 5.2 ユーザータグ管理
```http
POST /v1/tags
```
新しいユーザータグを作成

**リクエスト例**:
```json
{
  "name": "涙腺崩壊",
  "description": "感動で泣いてしまう作品",
  "category": "emotion",
  "public": true
}
```

```http
PUT /v1/tags/{tag_id}
```
自分が作成したタグを更新

## 6. 検索・発見

### 6.1 統合検索
```http
GET /v1/search
```
作品、ユーザー、リストを横断検索

**クエリパラメータ**:
- `q`: 検索キーワード
- `type`: 検索対象（`works`, `users`, `lists`, `all`）
- `filters`: 詳細フィルタ（JSON文字列）

**例**:
```http
GET /v1/search?q=価値観&type=works&filters={"genre":"anime","year_range":[2000,2024]}
```

### 6.2 レコメンデーション
```http
GET /v1/recommendations/works
```
おすすめ作品を取得

```http
GET /v1/recommendations/users
```
おすすめユーザーを取得

```http
GET /v1/recommendations/lists
```
おすすめリストを取得

## 7. 統計・分析

### 7.1 個人統計
```http
GET /v1/stats/personal
```
個人の活動統計を取得

**必要なスコープ**: `profile`

**レスポンス例**:
```json
{
  "success": true,
  "data": {
    "total_evaluations": 156,
    "total_lists": 8,
    "favorite_genres": ["anime", "manga", "novel"],
    "value_distribution": {
      "相互尊重": 0.3,
      "探求心": 0.25,
      "平和主義": 0.2
    }
  }
}
```

### 7.2 トレンド情報
```http
GET /v1/trends/works
```
トレンド作品を取得

```http
GET /v1/trends/tags
```
トレンドタグを取得

## 8. 通知・アクティビティ

### 8.1 通知管理
```http
GET /v1/notifications
```
通知一覧を取得

```http
PUT /v1/notifications/{notification_id}/read
```
通知を既読にする

```http
PUT /v1/notifications/read-all
```
すべての通知を既読にする

### 8.2 アクティビティフィード
```http
GET /v1/activities
```
フォロー中ユーザーのアクティビティを取得

**クエリパラメータ**:
- `type`: アクティビティタイプ
- `since`: 指定日時以降
- `limit`: 取得件数

## 9. 管理者API

### 9.1 システム管理
```http
GET /v1/admin/stats
```
システム全体の統計情報（管理者のみ）

**必要なスコープ**: `admin`

```http
POST /v1/admin/maintenance
```
メンテナンスモードの切り替え

## 10. エラーレスポンス例

### 10.1 バリデーションエラー
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "入力データに問題があります",
    "details": {
      "title": "作品名は必須です",
      "year": "1900年以降の年度を指定してください"
    }
  }
}
```

### 10.2 権限エラー
```json
{
  "success": false,
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "この操作を行う権限がありません",
    "details": {
      "required_scope": "works:write",
      "current_scopes": ["profile", "works:read"]
    }
  }
}
```

## 11. レート制限ヘッダー

すべてのレスポンスには以下のヘッダーが含まれます：

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

## 12. 例外的なレスポンス

### 12.1 メンテナンス中
```http
HTTP/1.1 503 Service Unavailable
```

```json
{
  "success": false,
  "error": {
    "code": "MAINTENANCE_MODE",
    "message": "現在メンテナンス中です",
    "details": {
      "maintenance_end": "2024-01-01T03:00:00Z"
    }
  }
}
```

詳細な使用例については、[GitHub リポジトリのサンプルコード](https://github.com/masakinihirota/api-examples)をご確認ください。
