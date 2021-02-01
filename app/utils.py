# 一些额外功能
from typing import List
from app import db


def add_year(year):
    def wapper(url):
        return f"{url}&year={year}"
    return wapper


def add_month(month):
    def wapper(url):
        return f'{url}&month={month}'
    return wapper


def formaturl_spider_jsonify(types: str, model: db.Model, spider_func,  **kwargs):
    if 'sex' not in kwargs.keys():
        urls = [f"https://www.qidian.com/rank/{types}?page={i}" for i in range(1,6)]
    else:
        urls = [f"https://www.qidian.com/mm/rank/{types}?page={i}" for i in range(1,6)]
    model.query.delete()
    if 'month' in kwargs.keys():
        urls = list(map(add_month(kwargs['month']), urls))
    if 'year' in kwargs.keys():
        urls = list(map(add_year(kwargs['year']), urls))
    for url in urls:
        spider_func(url,model)
    qds = model.query.all()
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
    return maps
