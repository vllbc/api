from app import app
from flask import request, redirect, jsonify
from app.models import QidianCollectionRank, QidianMonthlyTicketRank, Qidian24HourHotRank, QidianReadIndex, QidianRecom, \
    QidianSignNew, QidianPubNew, QidianFengYun


@app.route("/")
def index():
    return '主页未完成'


# 收藏榜
@app.route("/collection")
def collection():
    qds = QidianCollectionRank.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(collection_rank=maps)


# 起点月票榜
@app.route("/monthlyticket")
def monthlyticket():
    qds = QidianMonthlyTicketRank.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(monthlyticket_rank=maps)


# 24小时热销榜
@app.route("/hotsales")
def hotsales():
    qds = Qidian24HourHotRank.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(hotsales_rank=maps)


# 阅读指数榜
@app.route("/readindex")
def readindex():
    qds = QidianReadIndex.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(readindex_rank=maps)


# 推荐票榜
@app.route("/recom")
def recom():
    qds = QidianRecom.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(recom_rank=maps)


# 签约作者新书榜
@app.route("/signnew")
def signnew():
    qds = QidianSignNew.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(signnew_rank=maps)


# 公众作家新书榜
@app.route("/pubnew")
def pubnew():
    qds = QidianPubNew.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(pubnew_rank=maps)


# 原创风云榜 新书
@app.route("/fengyun")
def fengyun():
    qds = QidianFengYun.query.all()
    maps = list()
    for qd in qds:
        authors = {
            'name': qd.author,
            'authorid': qd.authorid
        }
        maps.append(
            {
                'ranking': qd.ranking,
                'title': qd.title,
                'author': authors,
                'classes': qd.classes,
                'bookid': qd.bookid,
                'state': qd.state
            }
        )
    return jsonify(fengyun_rank=maps)
