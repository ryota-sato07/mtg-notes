import sys
import os
from dotenv import load_dotenv
from audio_converter import convert_mp4_to_mp3
from audio_splitter import split_audio
from utils.file_utils import save_text_to_file
from utils.openai_utils import set_openai_key, transcribe_with_openai, summarize_with_openai

def main():
    # 環境変数をロードし、APIキーを取得
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # コマンドライン引数からMP4ファイルのパスを取得
    if len(sys.argv) < 2:
        print("MP4ファイルのパスを引数として指定してください。")
        sys.exit(1)

    mp4_file_path = sys.argv[1]
    output_folder = "./output/"
    interval_ms = 480_000  # 8分

    # MP4ファイルをMP3に変換し、指定された形式でサブディレクトリに保存
    mp3_file_path = convert_mp4_to_mp3(mp4_file_path, output_folder)

    # MP3ファイルを指定された時間間隔で分割
    mp3_file_path_list = split_audio(mp3_file_path, interval_ms, os.path.dirname(mp3_file_path))

    # OpenAI APIキーを設定
    set_openai_key(openai_api_key)

    # 分割された各MP3ファイルからトランスクリプションを生成し、結合
    combined_transcription = ""
    for path in mp3_file_path_list:
        transcription = transcribe_with_openai(path)
        combined_transcription += transcription + "\n"

    # 結合したトランスクリプションテキストを要約
    summarized_text = summarize_with_openai(combined_transcription)

    # 議事録をサブディレクトリに保存
    file_name = os.path.splitext(os.path.basename(mp4_file_path))[0]
    output_file_path = os.path.join(os.path.dirname(mp3_file_path), f"{file_name}_minutes.txt")
    save_text_to_file(summarized_text, output_file_path)

if __name__ == "__main__":
    main()
