from flaskr.extensions import db
from flask import Flask

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.Text(20))
    user_name = db.Column(db.Text(200))

    def __repr__(self):
        return f'<User "{self.user_id}">'
