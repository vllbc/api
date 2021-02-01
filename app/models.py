from app import db


# from werkzeug.security import generate_password_hash,check_password_hash

class QidianCollectionRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class QidianMonthlyTicketRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class Qidian24HourHotRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class QidianReadIndex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class QidianRecom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class QidianSignNew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class QidianPubNew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))


class QidianFengYun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.String(200))
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    classes = db.Column(db.String(200))
    bookid = db.Column(db.String(100))
    state = db.Column(db.String(20))
    authorid = db.Column(db.String(30))

# 待完成：新增粉丝榜，VIP更新榜，VIP收藏榜，VIP精品打赏榜，新人签约新书榜，新人作者新书榜，打赏粉丝榜，
