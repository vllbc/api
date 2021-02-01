from app import app
from flask import request, redirect, jsonify
from app.models import QidianCollectionRank, QidianMonthlyTicketRank, Qidian24HourHotRank, QidianReadIndex, QidianRecom, \
    QidianSignNew, QidianPubNew, QidianFengYun
from app.utils import *
from app.script.RankSpider import rankspider


@app.route("/")
def index():
    return '主页未完成'


# 收藏榜
@app.route("/collection")
def collection():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='collect', model=QidianCollectionRank, spider_func=rankspider, **args)
    return jsonify(collection_rank=maps)


# 起点月票榜
@app.route("/monthlyticket")
def monthlyticket():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='yuepiao', model=QidianMonthlyTicketRank, spider_func=rankspider, **args)
    return jsonify(monthlyticket_rank=maps)


# 24小时热销榜
@app.route("/hotsales")
def hotsales():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='hotsales', model=Qidian24HourHotRank, spider_func=rankspider, **args)
    return jsonify(hotsales_rank=maps)


# 阅读指数榜
@app.route("/readindex")
def readindex():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='readIndex', model=QidianReadIndex, spider_func=rankspider, **args)
    return jsonify(readindex_rank=maps)


# 推荐票榜
@app.route("/recom")
def recom():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='recom', model=QidianRecom, spider_func=rankspider, **args)
    return jsonify(recom_rank=maps)


# 签约作者新书榜
@app.route("/signnew")
def signnew():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='signnewbook', model=QidianSignNew, spider_func=rankspider, **args)
    return jsonify(signnew_rank=maps)


# 公众作家新书榜
@app.route("/pubnew")
def pubnew():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='pubnewbook', model=QidianPubNew, spider_func=rankspider, **args)
    return jsonify(pubnew_rank=maps)


# 原创风云榜 新书
@app.route("/fengyun")
def fengyun():
    args = dict(request.args)
    maps = formaturl_spider_jsonify(types='fengyun', model=QidianFengYun, spider_func=rankspider, **args)
    return jsonify(fengyun_rank=maps)
