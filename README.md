# mtg-notes

## Getting started

### Building a virtual environment

```
$ python3 -m venv ~/venv
$ source ~/venv/bin/activate
(venv)$
```

After executing the above command, configure the following settings for VSCode.

1. Installing [Python Extensions](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. Set the path for the virtual environment venv in [VSCode Setting > venv > Python: Venv Path]
3. Installation of each module

```
(venv)$ pip install openai==0.28.1
(venv)$ pip install moviepy
(venv)$ brew install ffmpeg
(venv)$ pip install pydub
(venv)$ pip install python-dotenv
```

### Execution of commands

Run the application as `python3 [file path to execute] [Video file path to create minutes]` as follows.

```
$ python3 mp4_to_minutes.py move/hoge.mp4
```
