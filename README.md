# spotify_playlist_buddy

## Bash File
[Spotify Bash File](https://github.com/StefonSimmons/spotify_bash_file)

> Add this script to your shell's confifuration file (.bashrc, .zshrc etc.)

## How to use:
> Save changes: restart terminal or run <code>source .bashrc</code>
> 
> Follow the prompts for each bash command:

**Create a playlist:**
```bash
spotify cp <name> "<description>"
```
> Example:
```bash
spotify cp Cookout-Playlist "Family and Summertime vibes"
```

**Search Spotify:**
```bash
spotify s "<query>"
```
> Example:
```bash
spotify s "Love Like Faith"

Searching for Love Like Faith...

Found:{
 Song: Love Like This
 Artist: Faith Evans
}

```

**List of user playlists:**
```bash
spotify list
```

**Play user Spotify player:**
```bash
spotify play
```

**Pause user Spotify player:**
```bash
spotify pause
```


## Flask App
> Server is not being used currently

- Create Virtual Environment for installations using venv module: 
```bash
py -m venv <name of virtual environment>
```

- Activate the Virtual Environment in GitBash ([Other Options for your shell](https://docs.python.org/3/library/venv.html#module-venv)):
```bash
source spotty/Scripts/activate
```

- Install Flask
```bash
pip install flask
```

- Tell flask to look at server.py when you run **flask run**
```bash
set FLASK_APP=server.py
```
- Export environment variable to FLASK_APP
```bash
export FLASK_APP=server.py
```
- RUN flask server (runs on http://127.0.0.1:5000/)
```bash
flask run
```
- Enable CORS with flask-cors
```bash
pip install -U flask-cors
```

- Deactivate the VE
```bash
deactivate
```



