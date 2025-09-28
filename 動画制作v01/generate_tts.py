# TTS音声生成スクリプト
# 要件: pip install gTTS

import os
from gtts import gTTS
from pathlib import Path

def generate_tts_narration():
    """narration.txtからTTS音声ファイル（narration.mp3）を生成"""

    # ファイルパスの設定
    script_dir = Path(__file__).parent
    narration_file = script_dir / "narration.txt"
    output_file = script_dir / "narration.mp3"

    try:
        # narration.txtを読み込み
        print("読み込み中: narration.txt")
        with open(narration_file, "r", encoding="utf-8") as f:
            text = f.read().strip()

        print(f"テキスト文字数: {len(text)} 文字")
        print("TTS音声生成中... (少し時間がかかります)")

        # gTTSでMP3生成（日本語）
        tts = gTTS(text=text, lang='ja', slow=False)
        tts.save(str(output_file))

        print(f"✓ 音声ファイル生成完了: {output_file}")
        print(f"ファイルサイズ: {output_file.stat().st_size / 1024:.1f} KB")

        return str(output_file)

    except FileNotFoundError:
        print(f"❌ エラー: {narration_file} が見つかりません")
        return None
    except Exception as e:
        print(f"❌ TTS生成エラー: {e}")
        return None

if __name__ == "__main__":
    print("=== VNS masakinihirota 動画ナレーション TTS生成 ===")
    result = generate_tts_narration()

    if result:
        print("\n次のステップ:")
        print("1. HTMLスライドテンプレート作成")
        print("2. inputs.txt（スライド表示時間）作成")
        print("3. ffmpegで画像と音声の合成")
    else:
        print("\n必要な準備:")
        print("pip install gTTS")
