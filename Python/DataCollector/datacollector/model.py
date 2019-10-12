from datacollector import db


class UserData(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height
