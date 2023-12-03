# import os
# import time
# import openai
# import moviepy.editor as mp
# from pydub import AudioSegment
# from dotenv import load_dotenv

# # MP4ファイルから音声を抽出する関数
# def extract_audio(mp4_file_path, audio_file_path):
#     video = mp.VideoFileClip(mp4_file_path)
#     audio = video.audio
#     audio.write_audiofile(audio_file_path)

# # Whisper APIを使って音声をテキストに変換する関数
# def transcribe_audio(audio_file_path, transcript_file_path):
#     command = f"whisper {audio_file_path} --model tiny --language en"
#     process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#     output, error = process.communicate()

#     if error:
#         print(f"エラーが発生しました: {error}")
#     else:
#         with open(transcript_file_path, "w") as file:
#             file.write(output.decode("utf-8"))

# # メイン関数
# def main():
#     mp4_file_path = "path/to/your/video.mp4"  # MP4ファイルのパス
#     audio_file_path = "path/to/your/audio.wav"  # 抽出する音声ファイルのパス
#     transcript_file_path = "path/to/your/transcript.txt"  # テキストファイルのパス

#     print("音声を抽出しています...")
#     extract_audio(mp4_file_path, audio_file_path)

#     print("音声をテキストに変換しています...")
#     transcribe_audio(audio_file_path, transcript_file_path)

#     print(f"議事録が作成されました: {transcript_file_path}")

# if __name__ == "__main__":
#     main()