# Spotify Playlist Buddy

## Setup
- Fork and Clone this repo
- <code>touch secret.py</code> in the flask_app directory
  - user_id = [from spotify user acount](https://www.spotify.com/)
  - client_id= [from spotify developer account](https://developer.spotify.com/dashboard/login)
  - client_secret= [from spotify developer account](https://developer.spotify.com/dashboard/login)

## Bash file
[Spotify Bash File](https://github.com/StefonSimmons/spotify_bash_file)

> Add this script to your shell's confifuration file (.bashrc, .zshrc etc.).
> 
> Allows you to run the Spotify Buddy program from the terminal

## How to run the program:
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
> <p style="color: red;">Server is not being used currently</p>

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



