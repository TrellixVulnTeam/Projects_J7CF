from flaskwsite import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    company = db.Column(db.String(20), unique=False, nullable=False)
    type = db.Column(db.String(20), unique=False, nullable=False)
    rdate = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"Game('{self.title}','{self.company}','{self.type}','{self.rdate}')"
