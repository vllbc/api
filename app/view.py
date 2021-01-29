from app import app
from flask import request, redirect, jsonify
from app.models import QidianModel


@app.route("/")
def index():
    return '主页未完成'


@app.route("/collection")
def collection():
    qds = QidianModel.query.all()
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
