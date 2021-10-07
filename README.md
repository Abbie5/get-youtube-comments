# get-youtube-comments

how to use:

- (optional) set up a venv
```sh
python3 -m venv venv
# there are different activation scripts for different platforms, use the one for your platform & shell
./venv/scripts/activate
```

- install requirements
```sh
pip install -r requirements.txt
```

- copy `keys.json.example` to `keys.json` and add in your api key, you can find out how to get one here: https://developers.google.com/youtube/v3/getting-started

- run with your favourite video to get all the comments in a `responses_<video id>.html` file
```sh
python main.py https://youtu.be/9N7oSJiKwiQ
```

# notes

currently the script errors on a video in a playlist or one with comments disabled, i may fix this later
