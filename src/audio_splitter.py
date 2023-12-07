from pydub import AudioSegment
import os

# 指定間隔で mp3 ファイルを分割し、指定パスにそれぞれ書き出す
def split_audio(mp3_file_path, interval_ms, output_folder):
    audio = AudioSegment.from_file(mp3_file_path)
    file_name, ext = os.path.splitext(os.path.basename(mp3_file_path))

    mp3_file_path_list = []
    n_splits = len(audio) // interval_ms
    for i in range(n_splits + 1):
        start = i * interval_ms
        end = (i + 1) * interval_ms
        split = audio[start:end]
        output_file_name = os.path.join(output_folder, f"{file_name}_{i}.mp3")
        split.export(output_file_name, format="mp3")
        mp3_file_path_list.append(output_file_name)

    return mp3_file_path_list
