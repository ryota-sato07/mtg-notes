from pydub import AudioSegment
import os

def split_audio(mp3_file_path, interval_ms, output_folder):
    audio = AudioSegment.from_file(mp3_file_path)
    file_name, ext = os.path.splitext(os.path.basename(mp3_file_path))

    # MP4ファイル名に基づいたサブディレクトリを作成
    sub_output_folder = os.path.join(output_folder, file_name)
    if not os.path.exists(sub_output_folder):
        os.makedirs(sub_output_folder)

    mp3_file_path_list = []
    n_splits = len(audio) // interval_ms
    for i in range(n_splits + 1):
        start = i * interval_ms
        end = (i + 1) * interval_ms
        split = audio[start:end]
        output_file_name = os.path.join(sub_output_folder, f"{file_name}_{i}.mp3")
        split.export(output_file_name, format="mp3")
        mp3_file_path_list.append(output_file_name)

    return mp3_file_path_list
