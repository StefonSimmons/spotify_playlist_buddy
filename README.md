# spotify_playlist_buddy

## Flask App

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



