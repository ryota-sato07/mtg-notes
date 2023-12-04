# mtg-notes

mp4 から txt 形式で議事録を出力するアプリケーション

## ディレクトリ構成

これがアプリケーションの一般的なフォルダー構造になります。

```
mtg-notes/
│
├── main.py 
├── audio_converter.py
├── audio_splitter.py
│
└── utils/
    ├── file_utils.py
    └── openai_utils.py
```

- **main.py**: アプリケーションの主要な処理フローを管理し、他のモジュールを統合します。
- **audio_converter.py**: MP4ファイルをMP3ファイルに変換する機能を担当します。
- **audio_splitter.py**: 長いMP3ファイルを小さな区間に分割する機能を提供します。
- **utils/file_utils.py**: テキストデータをファイルに保存する基本的な機能を提供します。
- **utils/openai_utils.py**: OpenAI APIを使用して音声の文字起こしとテキストの要約を行う機能を担当します。

## はじめる 

### 1. 環境変数の設定 

.envファイルを作成し、環境変数を設定する

```.env
OPENAI_API_KEY = "sk-******"
```

### 2. 仮想環境の構築

```
$ python3 -m venv ~/venv
$ source ~/venv/bin/activate
(venv)$
```

上記のコマンドを実行した後、VSCodeに対して以下の設定を行う。

1. [Python拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)のインストール
2. VSCode Setting > venv > Python: Venv Path]で仮想環境venvのパスを設定する。
3. 各モジュールのインストール

```
(venv)$ pip install openai==0.28.1
(venv)$ pip install moviepy
(venv)$ brew install ffmpeg
(venv)$ pip install pydub
(venv)$ pip install python-dotenv
```

### 3. コマンドの実行

以下のように`python3 [実行するファイルパス] [議事録を作成する動画ファイルパス]`としてアプリケーションを実行する。

```
$ python3 src/main.py move/hoge.mp4
```

## 検証メモ

目安として、9分10秒の動画で 「$0.06 のクレジットの消費」「1分46秒でプログラムが完了」の結果となった。

下記のようにディレクトリやファイルが生成される。

<img width="251" alt="image" src="https://github.com/ryota-sato07/mtg-notes/assets/87516579/ea42165a-2072-4f41-b9e4-3f426c91c080">