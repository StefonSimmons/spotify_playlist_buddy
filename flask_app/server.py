# https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
from flask import Flask, request
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from models import db, Code


# create an instance of the Flask class. __name__ references the name of the current module I'm working in (server.py)
app = Flask(__name__)
CORS(app)

# https://www.askpython.com/python-modules/flask/flask-postgresql
# configuring the PostgreSQL Connection
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:9021bEst@localhost:5432/spotify_buddy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def root ():
    return "<h1>I'm (g)root</h1>"

@app.route("/code/", methods=["POST"])
@cross_origin()
def create_code():
    if request.method == 'POST':
        req_json = request.get_json()
        code = req_json["code"]
        refresh_code = Code(refresh_code=code)
        db.session.add(refresh_code)
        db.session.commit()
        return "Done"

if __name__ == '__main__':
    app.run(debug=True)

