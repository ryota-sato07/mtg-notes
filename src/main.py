import sys
import os
from dotenv import load_dotenv
from audio_converter import convert_mp4_to_mp3
from audio_splitter import split_audio
from utils.file_utils import save_text_to_file
from utils.openai_utils import set_openai_key, transcribe_with_openai, summarize_with_openai

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if len(sys.argv) < 2:
        print("MP4ファイルのパスを引数として指定してください。")
        sys.exit(1)

    mp4_file_path = sys.argv[1]
    mp3_file_path = convert_mp4_to_mp3(mp4_file_path)
    output_folder = "./output/"
    interval_ms = 480_000  # 8分
    mp3_file_path_list = split_audio(mp3_file_path, interval_ms, output_folder)

    set_openai_key(openai_api_key)
    transcription_list = [transcribe_with_openai(path) for path in mp3_file_path_list]
    summarized_text = summarize_with_openai('\n'.join(transcription_list))

    # MP4ファイル名に基づいたサブディレクトリに議事録のTXTファイルを保存
    file_name = os.path.splitext(os.path.basename(mp4_file_path))[0]
    sub_output_folder = os.path.join(output_folder, file_name)
    output_file_path = os.path.join(sub_output_folder, f"{file_name}_minutes.txt")
    save_text_to_file(summarized_text, output_file_path)

if __name__ == "__main__":
    main()
