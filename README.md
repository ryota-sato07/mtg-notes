# mtg-notes

mp4 から txt 形式で議事録を出力するアプリケーション

## 実行環境

|       | バージョン・環境等 |
| :--   | :-- |
| PC    | MacBook Air (InterlCore i7) |
| MacOS | Ventura |
| python | 3.11.6 |
| openai | 1.3.7 |

<img width="196" alt="image" src="https://github.com/ryota-sato07/mtg-notes/assets/87516579/a718c736-1e4e-4e3c-8652-feac2554bfba">


## ディレクトリ構成

以下がアプリケーションのフォルダー構造になります。

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

| ファイル名 | 役割 |
| :--      | :-- |
| [**main.py**](https://github.com/ryota-sato07/mtg-notes/tree/main/src#mainpy)               | アプリケーションの主要な処理フローを管理し、他のモジュールを統合する |
| [**audio_converter.py**](https://github.com/ryota-sato07/mtg-notes/tree/main/src#audio_converterpy)    | MP4ファイルをMP3ファイルに変換する |
| [**audio_splitter.py**](https://github.com/ryota-sato07/mtg-notes/tree/main/src#audio_splitterpy)     | 長いMP3ファイルを小さな区間に分割する |
| [**utils/file_utils.py**](https://github.com/ryota-sato07/mtg-notes/tree/main/src#utilsfile_utilspy)   | テキストデータをファイルに保存する |
| [**utils/openai_utils.py**](https://github.com/ryota-sato07/mtg-notes/tree/main/src#utilsopenai_utilspy) | OpenAI APIを使用して音声の文字起こしとテキストの要約を行う |

## はじめる 

### 1. openai の API の利用設定

API を利用するために、openai にログインして [クレジットの追加](https://platform.openai.com/usage) と [API Key](https://platform.openai.com/api-keys) の登録が必要です。

登録方法は、別サイトを参照してください。

### 2. プロジェクトのクローン 

```
$ git clone git@github.com:ryota-sato07/mtg-notes.git 
$ cd mtg-note 
```

### 3. 環境変数の設定 

ルートディレクトリ直下に `.env` ファイルを作成し、環境変数を設定する

```.env: .env
OPENAI_API_KEY = "sk-******"
```

### 4. 仮想環境の構築

下記コマンドで仮想環境を立ち上げる。

```
$ python3 -m venv ~/venv
$ source ~/venv/bin/activate
(venv)$
```

その後、 VSCode に対して以下の設定を行う。

1. [Python拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python) のインストール
2. [VSCode Setting > venv > Python: Venv Path] で仮想環境 venv のパスを設定する。
3. 以下モジュールのインストール

```
(venv)$ pip install openai==0.28.1
(venv)$ pip install moviepy
(venv)$ brew install ffmpeg
(venv)$ pip install pydub
(venv)$ pip install python-dotenv
```

### 5. コマンドの実行

ルートディレクトリ配下の `/public/move` ディレクトリに mp4 形式のファイルを保存する。

その後、以下のように`python3 [実行するファイルパス] [議事録を作成する動画ファイルパス]`としてアプリケーションを実行する。

```
$ python3 src/main.py public/move/test_move.mp4
```

### 6. 仮想環境の無効化

下記コマンドで仮想環境を抜ける。

```
$ deactivate
```

## 検証メモ

目安として、9分10秒の動画で 「$0.05 のクレジットの消費」「2分01秒でプログラムが完了」の結果となった。

（ネット環境によってプログラムの完了時間は前後します。）

下記のようにディレクトリやファイルが生成される。

<img width="251" alt="image" src="https://github.com/ryota-sato07/mtg-notes/assets/87516579/ea42165a-2072-4f41-b9e4-3f426c91c080">
