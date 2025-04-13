このリポジトリの使い方

開発に必要なリポジトリを揃えます。

## プロジェクト全体のリポジトリ

- **コードリポジトリ:** Webアプリのリポジトリを用意します。
- **指示書リポジトリ:** GitHub Copilotの指示書リポジトリを用意します。
- **設計書リポジトリ:** 設計書を管理するリポジトリを用意します。
- **タスクリストリポジトリ:** タスクリストを管理するリポジトリを用意します。
- **ドキュメントリポジトリ:** ドキュメントを管理するリポジトリを用意します。
- **サンプルリポジトリ:** サンプルコードを管理するリポジトリを用意します。

このリポジトリはドキュメントのリポジトリです。



---

このファイルから初めます。

このREADME.mdファイルについて
* このプロジェクト全体のREADME.mdファイル
* ドキュメントのREADME.mdファイル
を兼ねています。

# プロジェクト全体のREADME.md

※このプロジェクトの開始場所
プロジェクト名 masakinihirota

# masakinihirotaプロジェクト全体のルール

ルール1
ドキュメントにかかれていることが最優先されます。

つまり、
`vns-masakinihirota-doc`リポジトリの`README.md`に書かれていることが最優先されます。

各リポジトリにはそれぞれ役割があります。

## 全リポジトリ

コードを書く場所
vns-masakinihirotaリポジトリ

指示書を書く場所
vns-masakinihirota-custom-instructionsリポジトリ

設計書を書く場所
vns-masakinihirota-designリポジトリ

タスクリストを書く場所
vns-masakinihirota-design-task-listリポジトリ

ドキュメントを書く場所
vns-masakinihirota-docリポジトリ

サンプルを書く場所
vns-masakinihirota-sampleリポジトリ

## リポジトリ関連図

```plantuml
@startuml
!define RECTANGLE class

skinparam componentStyle rectangle
skinparam monochrome true
skinparam shadowing false

RECTANGLE "vns-masakinihirota-design" as design {
  設計書
  要件定義
  仕様書
}

RECTANGLE "vns-masakinihirota-design-task-list" as tasklist {
  タスクリスト
  進行状況管理
}

RECTANGLE "vns-masakinihirota-custom-instructions" as instructions {
  GitHub Copilot指示書
  プロンプトファイル
}

RECTANGLE "vns-masakinihirota" as webapp {
  Webアプリケーションコード
  実装
  テスト
}

RECTANGLE "vns-masakinihirota-doc" as doc {
  公開ドキュメント
  ユーザーガイド
}

design -down-> tasklist : 1. タスク分解
tasklist -down-> instructions : 2. プロンプト\n作成
instructions -down-> webapp : 3. コード生成
webapp --> webapp : 4. コードレビュー
webapp -right-> doc : 5. ドキュメント\n生成
webapp -left-> design : 6. フィードバック
design -down-> doc : 情報提供

note right of design : 人間の思考を文書化
note left of webapp : GitHub Copilotが\n生成したコード
note left of instructions : GitHub Copilotへの\n指示内容
@enduml

```

この図は各リポジトリ間の関係と情報の流れを示しています。設計書から始まり、タスク分解、プロンプト作成、コード生成という流れと、フィードバックループやドキュメント生成の関係を表現しています。












# 全リポジトリの管理

VSCodeのワークスペース機能を使って複数のリポジトリをまとめて管理します。

※GitHub Copilotはワークスペース内のファイルを見ています。

## ワークスペースの設定

VSCodeを開き、それぞれのリポジトリを登録します。

## 複数リポジトリをVSCodeのワークスペースで利用する方法

### ワークスペースの作成手順
1. **VS Codeを起動**し、「ファイル」→「ワークスペースをフォルダーに追加...」を選択。
2. 指示書リポジトリとコードリポジトリを追加。
3. 「ワークスペースを名前を付けて保存...」でワークスペースファイルを保存（例: `my-project.code-workspace`）。
4. ワークスペースを開き、GitHub Copilotに指示書を読ませてコード生成を指示。

👇ワークスペース設定のファイルに登録できています。

```[ワークスペース名].code-workspace
{
	"folders": [
		{
			"path": "リポジトリ名1"
		},
		{
			"path": "リポジトリ名2"
		}
	],
	"settings": {
		// ワークスペース専用の設定を書けます。
	}
}

```

ワークスペースの設定ファイルを
ワークスペースに登録したリポジトリのルートに置きます。

作成されたワークスペースファイルは、リポジトリのルートに保存されます。
`_vns-masakinihirota.code-workspace`



----------------------------------------

# ドキュメントのREADME.md





##





##



