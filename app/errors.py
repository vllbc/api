from app import db,app
from flask import jsonify


@app.errorhandler(404)
def error404(e):
    d = {
        'code': '404',
        'data': 'Page Not Found!'
    }
    return jsonify(d),404


@app.errorhandler(500)
def error500(e):
    d = {
        'code': '500',
        'data': 'Error!'
    }
    return jsonify(d)