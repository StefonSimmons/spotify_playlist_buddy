# https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
from flask import Flask
from flask_cors import CORS

import create_playlist

# create an instance of the Flask class. __name__ references the name of the current module I'm working in (server.py)
app = Flask(__name__)
CORS(app)


@app.route("/")
def root ():
    return "<h1>I'm (g)root</h1>"

@app.route("/code/<auth_code>")
def pass_code(auth_code):
    create_playlist.CreatePlaylist().refresh_code = auth_code
    create_playlist.CreatePlaylist().get_new_token()
    return {
        "code":auth_code
    }


# when a user gets to my index.html file
# on click of a button, execute a request.
# the request is going to reque