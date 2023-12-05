# 実装詳細

## main.py

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
- OpenAPI Key を設定

### OpenAPI との接続

- トランスクリプション？？？

```python
```

## audio_converter.py

```python
```

## audio_splitter.py

```python
```

## utils/file_utils.py

```python
```

## utils/openai_utils.py 

```python
```
