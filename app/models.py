from app import db


class QidianModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))



