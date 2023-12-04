import openai

def set_openai_key(api_key):
    openai.api_key = api_key

def transcribe_with_openai(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription.text

def summarize_with_openai(transcription_part):
    prompt = """
    あなたは、プロの議事録作成者です。
    「テキストの全体の本文」と「要点のまとめ」を作成して欲しいです。
    以下の「制約条件」「出力フォーマット」「内容」を元に文章を出力してください。

    # 制約条件
    ・誤字・脱字があるため、話の内容を予測して置き換えてください。
    ・「要点のまとめ」は、要点をまとめ、簡潔に書いて下さい。
    ・「テキスト全体」は、意味が通じる文章として適切に改行し、すべて記載してください。

    # 出力フォーマット

    ## テキスト全体
    ここに本文を記載

    ## 要点のまとめ
    ここに要点まとめを記載

    # 内容
    """ + transcription_part
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.0,
    )
    return response['choices'][0]['message']['content']
