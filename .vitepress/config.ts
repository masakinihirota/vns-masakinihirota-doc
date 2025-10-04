import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "masakinihirota",
  description: "価値観共有プラットフォーム - ドキュメント",
  lang: 'ja-JP',

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'ホーム', link: '/' },
      { text: 'ユーザーガイド', link: '/user-guide/getting-started' },
      { text: '開発者ガイド', link: '/developer-guide/overview' },
      { text: 'API', link: '/api/overview' }
    ],

    sidebar: {
      // ユーザーガイド
      '/user-guide/': [
        {
          text: 'はじめに',
          items: [
            { text: 'はじめに', link: '/user-guide/getting-started' },
            { text: 'アカウント作成・ログイン', link: '/user-guide/account' }
          ]
        },
        {
          text: '主要機能',
          items: [
            { text: 'プロフィール管理', link: '/user-guide/profile' },
            { text: '作品登録・評価', link: '/user-guide/works' },
            { text: 'マッチング機能', link: '/user-guide/matching' },
            { text: 'リスト機能', link: '/user-guide/lists' },
            { text: 'タグ機能', link: '/user-guide/tags' }
          ]
        },
        {
          text: 'その他',
          items: [
            { text: 'FAQ', link: '/faq' }
          ]
        }
      ],

      // 開発者ガイド（自動生成後に追加）
      '/developer-guide/': [
        {
          text: '開発ガイド',
          items: [
            { text: '概要', link: '/developer-guide/overview' },
            { text: '環境構築', link: '/developer-guide/setup' },
            { text: 'アーキテクチャ', link: '/developer-guide/architecture' }
          ]
        },
        {
          text: 'コンポーネント',
          items: [
            // ドキュメント生成後に追加
            // { text: 'プロフィール管理', link: '/developer-guide/profile' },
            // { text: '作品登録', link: '/developer-guide/works' },
          ]
        },
        {
          text: 'データベース',
          items: [
            { text: 'スキーマ概要', link: '/developer-guide/database-schema' },
            // { text: 'テーブル定義', link: '/developer-guide/tables' }
          ]
        }
      ],

      // API
      '/api/': [
        {
          text: 'API リファレンス',
          items: [
            { text: '概要', link: '/api/overview' },
            { text: '認証', link: '/api/authentication' },
            { text: 'エンドポイント', link: '/api/endpoints' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/masakinihirota/vns-masakinihirota' }
    ],

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '検索',
                buttonAriaLabel: '検索'
              },
              modal: {
                noResultsText: '結果が見つかりません',
                resetButtonTitle: 'リセット',
                footer: {
                  selectText: '選択',
                  navigateText: '移動',
                  closeText: '閉じる'
                }
              }
            }
          }
        }
      }
    },

    footer: {
      message: 'オアシス宣言・人間宣言のもと、安心で安全なオンライン空間を提供します。',
      copyright: 'Copyright © 2025 masakinihirota'
    },

    lastUpdated: {
      text: '最終更新',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'short'
      }
    },

    docFooter: {
      prev: '前のページ',
      next: '次のページ'
    },

    outline: {
      label: '目次',
      level: [2, 3]
    }
  },

  // Markdown設定
  markdown: {
    lineNumbers: true,
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  }
})
