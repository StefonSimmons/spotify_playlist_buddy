# Spotify Playlist Buddy

Are you a Developer? Do you have a Spotify account? Have you ever had the desire to play Spotify from the terminal? Yes?? Well, you're in the right place!

A terminal-based program mostly written in Python.

<img src="https://media.giphy.com/media/WjQYG5UBbdtcRzscAC/giphy.gif" width="550px" alt="spotify-buddy"/>

## Tech

| Tech             | Description                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Spotify Web API** | A REST API used to interact with music artists, albums, and tracks, directly from the Spotify Data Catalogue. |
| **webbrowser**      | Convenient web-browser controller to open url in browser                                                                            |
| **requests** | Allows for HTTP requests to the Spotify API |

## Setup

1. Fork and Clone this repo locally

### Setup Bash file
Click here for more: [Spotify Bash File](https://github.com/StefonSimmons/spotify_bash_file)

> Add this script to your shell's configuration file (.bashrc, .zshrc etc.).
>
> Allows you to run the Spotify Buddy program from the terminal

### Setup Environment

**Create required authentication files and virtual environment:**

```bash
make setup
```
in secret.py
- user_id = [from spotify user account](https://www.spotify.com/)
- client_id= [from spotify developer account](https://developer.spotify.com/dashboard/login) (Create an app on the dashboard)
- client_secret= [from spotify developer account](https://developer.spotify.com/dashboard/login) (Create an app on the dashboard)
- redirect_uri= "https://spotify-playlist-buddy.vercel.app/" (You may use this uri as your redirects_uri or your own)

**Activate the Virtual Environment**
  > for zsh or bash

```bash
source spotify_python/senv/bin/activate
```
  > [Other Options for your shell](https://docs.python.org/3/library/venv.html#module-venv)

**Install program dependencies/packages:**
  > **NOTE** make sure you are in your virtual environment

```bash
make install
```

**Restart Terminal**
```bash
source .bashrc
```
OR
```bash
source .zshrc
``` 
OR

simply restart terminal


**In order to deactivate the virtual environment**

```bash
deactivate
```

## Usage:

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

# Searching for Love Like Faith...

# Found:{
#  Song: Love Like This
#  Artist: Faith Evans
# }
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
