# 一些额外功能
from typing import List, Any


def add_year(year):
    def wapper(url):
        return f"{url}&year={year}"

    return wapper


def add_month(month):
    def wapper(url):
        return f'{url}&month={month}'

    return wapper


def formaturl_spider_jsonify(types: str, spider_func: Any, **kwargs: Any) -> List[dict]:
    if 'sex' not in kwargs.keys():
        urls = [f"https://www.qidian.com/rank/{types}?page={i}" for i in range(1, 6)]
    elif kwargs['sex'] == 'mm':
        urls = [f"https://www.qidian.com/mm/rank/{types}?page={i}" for i in range(1, 6)]
    else:
        return [{"data": 'error!What is the sex?'}]
    if 'month' in kwargs.keys():
        urls = list(map(add_month(kwargs['month']), urls))
    if 'year' in kwargs.keys():
        urls = list(map(add_year(kwargs['year']), urls))
    authors = {}
    res = []
    for url in urls:
        ns = spider_func(url)
        for n in ns:
            authors['name'] = n.author
            authors['author_id'] = n.authorid
            m = {
                'title': n.title,
                'author': authors,
                'classes': n.classes,
                'bookid': n.bookid,
                'state': n.state,
                'ranking': n.ranking
            }
            res.append(m)
    return res
