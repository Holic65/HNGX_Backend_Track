from flask_sqlalchemy import  SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    userid = db.Column(db.String())

    def __init__(self, name, userid):
        self.name = name
        self.userid = userid

    def __repr__(self):
        return {
            'name': self.name,
            'userid': self.userid
        }