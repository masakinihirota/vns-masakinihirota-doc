#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VNS 動画生成スクリプト
inputs.txt作成 & ffmpeg実行を自動化
"""
import os
import json
import subprocess
import sys

def create_inputs_txt():
    """inputs.txtファイルを作成"""

    # スライドタイミング設定
    slide_timings = [
        20,  # slide01: イントロ - 20秒
        15,  # slide02: 問題提起 - 15秒
        20,  # slide03: 解決案 - 20秒
        25,  # slide04: 主要機能 - 25秒
        20,  # slide05: MVP範囲 - 20秒
        25,  # slide06: 技術構成 - 25秒
        30,  # slide07: データ構造 - 30秒
        20,  # slide08: セキュリティ - 20秒
        25,  # slide09: UI/UX - 25秒
        30,  # slide10: 開発・運用 - 30秒
        20,  # slide11: 今後の展開 - 20秒
        15   # slide12: まとめ - 15秒
    ]

    # inputs.txt作成
    with open('inputs.txt', 'w', encoding='utf-8') as f:
        for i, duration in enumerate(slide_timings, 1):
            slide_name = f"slide{i:02d}.png"
            f.write(f"file '{slide_name}'\n")
            f.write(f"duration {duration}\n")

        # 最後のフレームを少し延長
        f.write(f"file 'slide12.png'\n")

    print("✓ inputs.txt作成完了")

    # 合計時間を計算
    total_time = sum(slide_timings)
    print(f"合計再生時間: {total_time}秒 ({total_time//60}分{total_time%60}秒)")

def run_ffmpeg():
    """ffmpegで動画を生成"""

    # ffmpegコマンド構成
    cmd = [
        'ffmpeg',
        '-y',  # 上書き許可
        '-f', 'concat',
        '-safe', '0',
        '-i', 'inputs.txt',
        '-i', 'narration.mp3',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-r', '30',  # フレームレート
        '-c:a', 'aac',
        '-b:a', '128k',
        '-shortest',  # 短い方に合わせる
        '-video_track_timescale', '30000',
        'vns_requirements_video.mp4'
    ]

    print("=== ffmpeg実行開始 ===")
    print("コマンド:", ' '.join(cmd))
    print()

    try:
        result = subprocess.run(cmd,
                              check=True,
                              capture_output=True,
                              text=True,
                              encoding='utf-8')

        print("✓ 動画生成完了: vns_requirements_video.mp4")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ ffmpegエラー:")
        print(f"リターンコード: {e.returncode}")
        print(f"stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ ffmpegが見つかりません")
        print("ffmpegをインストールしてPATHに追加してください")
        return False

def check_files():
    """必要なファイルの存在確認"""
    required_files = [
        'narration.mp3',
        'slide_template.html'
    ]

    # スライド画像の確認
    for i in range(1, 13):
        required_files.append(f'slide{i:02d}.png')

    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print("❌ 必要なファイルが不足しています:")
        for file in missing_files:
            print(f"  - {file}")
        return False

    print("✓ すべての必要ファイルが存在します")
    return True

def main():
    """メイン処理"""
    print("=== VNS 動画合成スクリプト ===")
    print()

    # ファイル確認
    if not check_files():
        sys.exit(1)

    # inputs.txt作成
    create_inputs_txt()

    # ffmpeg実行
    success = run_ffmpeg()

    if success:
        print()
        print("🎉 動画制作完了！")
        print("📄 ファイル: vns_requirements_video.mp4")
        print("📐 解像度: 1920x1080")
        print("🎵 音声: 日本語TTS")
        print("⏱️  長さ: 約5分")
    else:
        print("❌ 動画制作に失敗しました")
        sys.exit(1)

if __name__ == '__main__':
    main()
