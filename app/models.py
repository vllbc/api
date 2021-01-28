from app import db


class QidianModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))


