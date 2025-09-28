// Puppeteer スライド画像生成スクリプト
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
        console.log('\n=== すべてのスライド画像生成完了 ===');
        console.log('次のステップ: inputs.txt作成 & ffmpeg合成');
        
    } catch (error) {
        console.error('❌ エラー:', error);
        process.exit(1);
    }
}

renderSlides();