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
        maps.append(
            {
                'id': qd.id,
                'title': qd.title,
                'author': qd.author,
                'classes': qd.classes
            }
        )
    return jsonify(allbooks=maps)
