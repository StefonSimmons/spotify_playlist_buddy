# Spotify Playlist Buddy

Are you a Developer? Do you have a Spotify account? Have you ever had the desire to play Spotify from the terminal? Yes?? Well, you're in the right place! 

A terminal-based program mostly written in Python.

<img src="https://media.giphy.com/media/WjQYG5UBbdtcRzscAC/giphy.gif" width="550px" alt="spotify-buddy"/>

## Setup
- Fork and Clone this repo
- <code>touch secret.py</code> in the flask_app directory
- Add the following values to the <code>secret.py</code> file:
  - user_id = [from spotify user account](https://www.spotify.com/)
  - client_id= [from spotify developer account](https://developer.spotify.com/dashboard/login) (Create an app on the dashboard)
  - client_secret= [from spotify developer account](https://developer.spotify.com/dashboard/login) (Create an app on the dashboard)
  - redirect_uri= "https://spotify-playlist-buddy.vercel.app/" (You may use this uri as your redirects_uri or your own)

**Setup Bash file**
Click here for more: [Spotify Bash File](https://github.com/StefonSimmons/spotify_bash_file)

> Add this script to your shell's configuration file (.bashrc, .zshrc etc.).
> 
> Allows you to run the Spotify Buddy program from the terminal

**Setup Environment**

- Create Virtual Environment for installations using venv module: 
```bash
python3 -m venv <name of virtual environment>
```
- Activate the Virtual Environment
  - in zsh or bash
  ```bash
  source <name of virtual environment>/bin/activate
  ```
  - [Other Options for your shell](https://docs.python.org/3/library/venv.html#module-venv)

- Install program dependencies/packages:
  > **NOTE** make sure you are in your virtual environment
```bash
pip install -r requirements.txt
``` 
- Deactivate the Virtual Environment
```bash
deactivate
```


## Usage:
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



