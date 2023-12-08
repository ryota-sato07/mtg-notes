import os
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数をロードし、APIキーを取得
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key = openai_api_key 
)

openai_audio = OpenAI()

# Whisper で音声からテキストを書き起こす
def transcribe_with_openai(audio_file_path):
    # with open(audio_file_path, 'rb') as audio_file:
    #     audio_data = audio_file.read()

    transcription = openai_audio.transcriptions.create(model="whisper-1", file=audio_file_path)
    return transcription.text

# 文字起こしをプロンプトを元に ChatGPT を実行する
def summarize_with_openai(transcription_part):
    prompt = """
    あなたは、プロの議事録作成者です。
    「要点のまとめ」と「テキスト全体」を作成して欲しいです。
    以下の「制約条件」「出力フォーマット」「内容」を元に文章を出力してください。

    # 制約条件
    ・誤字・脱字があるため、話の内容を予測して置き換えてください。
    ・出力する文章が途中で切れてしまうときは、続きも記載してください。
    ・「要点のまとめ」は、要点をまとめ、簡潔に書いて下さい。
    ・「テキスト全体」は、意味が通じる文章として適切に改行し、すべて記載してください。

    # 出力フォーマット

    ## 要点のまとめ
    ここに要点まとめを記載

    ## テキスト全体
    ここに本文を記載

    # 内容
    """ + transcription_part
    response = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": prompt,
        }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content
