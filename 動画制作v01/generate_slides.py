# スライド生成スクリプト
# 要件: npm install puppeteer

import json
import os
from pathlib import Path

def create_slides_data():
    """12枚のスライドデータを定義"""

    slides = [
        {
            "id": "slide01",
            "title": "VNS masakinihirota",
            "subtitle": "価値観でつながる新しいネットワークサービス",
            "body": "<h3>MVP版要件定義書の紹介</h3>",
            "duration": 12
        },
        {
            "id": "slide02",
            "title": "VNSとは？",
            "subtitle": "Value Network Service",
            "body": """
            <ul>
                <li>個人情報に依存しないマッチング</li>
                <li>作品・価値観ベースでの安全な繋がり</li>
                <li>オアシス宣言準拠の安心・安全な場</li>
                <li>最小限の登録で価値検証を実現</li>
            </ul>
            """,
            "duration": 25
        },
        {
            "id": "slide03",
            "title": "SNS vs VNS",
            "subtitle": "異なるアプローチ",
            "body": """
            <div class="comparison">
                <div>
                    <h3>SNS</h3>
                    <ul>
                        <li>社会的つながり重視</li>
                        <li>表現の自由重視</li>
                    </ul>
                </div>
                <div>
                    <h3>VNS</h3>
                    <ul>
                        <li>価値観でのつながり</li>
                        <li>安全性重視</li>
                        <li>建設的な議論</li>
                        <li>ボトムアップ運営</li>
                    </ul>
                </div>
            </div>
            """,
            "duration": 25
        },
        {
            "id": "slide04",
            "title": "非認証体験機能",
            "subtitle": "登録前の体験",
            "body": """
            <ul>
                <li>ダミープロフィールの閲覧</li>
                <li>ダミーデータでマッチング体験</li>
                <li>作品・価値観サンプル閲覧</li>
                <li>保存・編集は不可（体験のみ）</li>
            </ul>
            """,
            "duration": 20
        },
        {
            "id": "slide05",
            "title": "認証・初期設定",
            "subtitle": "Supabase Auth対応",
            "body": """
            <ul>
                <li>Google・GitHub認証</li>
                <li>居住地域（地球3分割）</li>
                <li>母語・UI言語設定</li>
                <li>生誕世代設定</li>
                <li>オアシス宣誓（必須）</li>
                <li>広告ON/OFF選択</li>
            </ul>
            """,
            "duration": 25
        },
        {
            "id": "slide06",
            "title": "ルートアカウント機能",
            "subtitle": "1ユーザー = 1ルート",
            "body": """
            <ul>
                <li>ポイント表示（次版で消費ロジック）</li>
                <li>経過日数の管理</li>
                <li>全データリセット機能</li>
                <li>複数プロフィールの管理</li>
                <li>信頼度の自動算出</li>
            </ul>
            """,
            "duration": 20
        },
        {
            "id": "slide07",
            "title": "ユーザープロフィール",
            "subtitle": "目的別の多面的アプローチ",
            "body": """
            <ul>
                <li>複数作成可能（上限4）</li>
                <li>仕事・友人・婚活・終活・その他</li>
                <li>表示形式：名刺・履歴書・フル</li>
                <li>自動グループ生成（リーダー権限付き）</li>
            </ul>
            """,
            "duration": 25
        },
        {
            "id": "slide08",
            "title": "登録機能",
            "subtitle": "作品・価値観の管理",
            "body": """
            <div class="tech-grid">
                <div class="tech-item">
                    <h3>作品登録</h3>
                    <ul>
                        <li>公式約100件</li>
                        <li>ユーザー追加登録</li>
                        <li>アニメ・マンガ対応</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <h3>価値観登録</h3>
                    <ul>
                        <li>設問・選択肢モデル</li>
                        <li>重要度フラグ</li>
                        <li>カテゴリ別管理</li>
                    </ul>
                </div>
            </div>
            """,
            "duration": 20
        },
        {
            "id": "slide09",
            "title": "マッチング機能",
            "subtitle": "高精度スコア算出システム",
            "body": """
            <ul>
                <li>0-100点スコア算出</li>
                <li>ランク表示：High / Medium / Low / Very Low</li>
                <li>自動マッチング（75点以上、最大5人）</li>
                <li>作品Tier一致度・価値観一致度</li>
                <li>重要フラグによる加点システム</li>
            </ul>
            """,
            "duration": 30
        },
        {
            "id": "slide10",
            "title": "UI・国際化機能",
            "subtitle": "ユーザビリティ重視",
            "body": """
            <div class="tech-grid">
                <div class="tech-item">
                    <h3>グループ関連</h3>
                    <ul>
                        <li>オアシス宣言自動適用</li>
                        <li>関係語彙管理</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <h3>UI対応</h3>
                    <ul>
                        <li>日本語・英語対応</li>
                        <li>レスポンシブデザイン</li>
                        <li>ダークモード対応</li>
                    </ul>
                </div>
            </div>
            """,
            "duration": 20
        },
        {
            "id": "slide11",
            "title": "技術仕様",
            "subtitle": "セキュリティ・パフォーマンス重視",
            "body": """
            <div class="tech-grid">
                <div class="tech-item">
                    <h3>データモデル</h3>
                    <ul>
                        <li>ルートアカウント・プロフィール</li>
                        <li>作品・価値観の関係管理</li>
                        <li>RLS セキュリティ制御</li>
                    </ul>
                </div>
                <div class="tech-item">
                    <h3>非機能要件</h3>
                    <ul>
                        <li>P90応答時間 200ms以内</li>
                        <li>OAuth・XSS対策</li>
                        <li>99.9%可用性目標</li>
                    </ul>
                </div>
            </div>
            """,
            "duration": 30
        },
        {
            "id": "slide12",
            "title": "受入基準・今後の展望",
            "subtitle": "MVP完成目標",
            "body": """
            <ul>
                <li><span class="checkmark">✓</span>非認証ダミー体験</li>
                <li><span class="checkmark">✓</span>OAuth認証・初期設定</li>
                <li><span class="checkmark">✓</span>プロフィール・作品・価値観登録</li>
                <li><span class="checkmark">✓</span>マッチング機能</li>
                <li><span class="checkmark">✓</span>安全なリセット機能</li>
            </ul>
            <h3 style="margin-top: 40px; color: #FFE066;">次フェーズ: 高度なグループ運営・課金機能</h3>
            """,
            "duration": 15
        }
    ]

    return slides

def create_slides_json():
    """slides.jsonファイルを作成"""
    slides = create_slides_data()

    # JSON形式で保存
    script_dir = Path(__file__).parent
    json_file = script_dir / "slides.json"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(slides, f, ensure_ascii=False, indent=2)

    print(f"✓ slides.json作成完了: {json_file}")
    return slides

def create_render_script():
    """Node.js用のスライド画像生成スクリプトを作成"""

    render_script = """// Puppeteer スライド画像生成スクリプト
// 実行: node render_slides.js
// 要件: npm install puppeteer

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

async function renderSlides() {
    console.log('=== VNS スライド画像生成開始 ===');

    try {
        // slides.json読み込み
        const slidesData = JSON.parse(fs.readFileSync('slides.json', 'utf8'));
        console.log(`スライド数: ${slidesData.length} 枚`);

        // HTMLテンプレート読み込み
        const templateHtml = fs.readFileSync('slide_template.html', 'utf8');

        // Puppeteer起動
        console.log('Puppeteer起動中...');
        const browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();

        // ビューポート設定（1920x1080）
        await page.setViewport({ width: 1920, height: 1080 });

        // 各スライドを画像として保存
        for (let i = 0; i < slidesData.length; i++) {
            const slide = slidesData[i];
            console.log(`生成中: ${slide.id} (${i + 1}/${slidesData.length})`);

            // HTMLに内容を挿入
            const slideHtml = templateHtml
                .replace('id="slide-title">タイトル', `id="slide-title">${slide.title}`)
                .replace('id="slide-subtitle">サブタイトル', `id="slide-subtitle">${slide.subtitle}`)
                .replace('<!-- スライドごとの内容がここに挿入される -->', slide.body);

            // ページにHTML設定
            await page.setContent(slideHtml, {
                waitUntil: 'networkidle0',
                timeout: 30000
            });

            // 画像として保存
            const fileName = `${slide.id.replace('slide', 'slide')}.png`;
            await page.screenshot({
                path: fileName,
                fullPage: false,
                type: 'png'
            });

            console.log(`✓ 保存完了: ${fileName}`);
        }

        await browser.close();
        console.log('\\n=== すべてのスライド画像生成完了 ===');
        console.log('次のステップ: inputs.txt作成 & ffmpeg合成');

    } catch (error) {
        console.error('❌ エラー:', error);
        process.exit(1);
    }
}

renderSlides();"""

    script_dir = Path(__file__).parent
    js_file = script_dir / "render_slides.js"

    with open(js_file, "w", encoding="utf-8") as f:
        f.write(render_script)

    print(f"✓ render_slides.js作成完了: {js_file}")

def create_package_json():
    """package.jsonを作成（Puppeteerインストール用）"""

    package_data = {
        "name": "vns-slide-generator",
        "version": "1.0.0",
        "description": "VNS masakinihirota スライド画像生成",
        "main": "render_slides.js",
        "scripts": {
            "start": "node render_slides.js",
            "install-puppeteer": "npm install puppeteer"
        },
        "dependencies": {
            "puppeteer": "^21.0.0"
        }
    }

    script_dir = Path(__file__).parent
    package_file = script_dir / "package.json"

    with open(package_file, "w", encoding="utf-8") as f:
        json.dump(package_data, f, indent=2)

    print(f"✓ package.json作成完了: {package_file}")

if __name__ == "__main__":
    print("=== VNS スライドテンプレート生成 ===")

    # 各ファイルを作成
    slides = create_slides_json()
    create_render_script()
    create_package_json()

    print(f"\\n作成完了:")
    print(f"- slide_template.html (HTMLテンプレート)")
    print(f"- slides.json ({len(slides)}枚のスライドデータ)")
    print(f"- render_slides.js (画像生成スクリプト)")
    print(f"- package.json (依存関係)")

    print(f"\\n次の実行手順:")
    print(f"1. npm install puppeteer")
    print(f"2. node render_slides.js")
    print(f"3. inputs.txt作成")
    print(f"4. ffmpeg合成")
