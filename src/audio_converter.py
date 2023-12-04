import moviepy.editor as mp
import os
from datetime import datetime

def convert_mp4_to_mp3(mp4_file_path, output_folder):
    # 現在の日時をyyyyMMdd-hhmmss形式で取得
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    file_name = os.path.splitext(os.path.basename(mp4_file_path))[0]
    # 日時を含むサブディレクトリ名を作成
    sub_output_folder = os.path.join(output_folder, f"{current_datetime}-{file_name}")
    
    if not os.path.exists(sub_output_folder):
        os.makedirs(sub_output_folder)

    mp3_file_path = os.path.join(sub_output_folder, file_name + '.mp3')
    audio = mp.AudioFileClip(mp4_file_path)
    audio.write_audiofile(mp3_file_path)
    return mp3_file_path
