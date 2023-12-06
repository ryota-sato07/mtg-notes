# 実装詳細

## □ main.py

### Python ライブラリでの事前準備

- .env ファイルを読み込んで、取得した API key を変数にセットする
- コマンドライン引数から mp4 の動画ファイルパスを取得
  - 引数がなければエラーメッセージを表示
  - 確認する引数は、配列の 1番目までで、プログラムを強制終了する。
- 変数定義
  - 動画のファイルパス指定
  - mp3 動画や txt ファイルの出力先パス指定
  - 動画ファイルの分割間隔（8分に設定することで Whisper と ChatGPT のどちらの制限にもかからないため）
- `現在時刻_ファイル名` でディレクトリを生成し、その配下に mp4 から mp3 を生成したものを配置 
  - 詳細は audio_converter.py
- 生成したディレクトリ配下に、mp3 を 8分ごとに分割したファイルを配置
  - 詳細は audio_splitter.py

### OpenAPI との接続

- OpenAPI Key を設定
- 分割した mp3 ファイルから、それぞれ文字起こしを行い、それらを結合して変数に格納する
  - 詳細は utils/openai_utils.py
- 結合したテキストを、定義したプロンプトをもとに ChatGPT で要約
  - 詳細は utils/openai_utils.py
- 生成したディレクトリに議事録を保存
  - 詳細は utils/file_utils.py
- スクリプトが直接実行された場合にのみmain関数を呼び出す

## □ audio_converter.py

- 

## □ audio_splitter.py

```python
```

## □ utils/file_utils.py

```python
```

## □ utils/openai_utils.py 

```python
```
