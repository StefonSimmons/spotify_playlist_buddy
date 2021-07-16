from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Code(db.Model):
    __tablename_ = 'code_table'

    id = db.Column(db.Integer, primary_key = True)
    refresh_code = db.Column(db.String())

    def __init__(self, refresh_code):
        self.refresh_code = refresh_code 

    def __repr__(self):
        return f"{self.refresh_code}"
        