from threading import Lock
import requests
from lxml import etree
from app import db
import re
from collections import namedtuple


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

lock = Lock()

model = namedtuple("model",['title', 'author', 'classes', 'bookid', 'state', 'authorid', 'ranking'])


def rankspider(url):
    res = requests.get(url, headers=headers)
    sel = etree.HTML(res.text)
    infos = sel.xpath('//*[@id="rank-view-list"]/div/ul/li')
    res = []
    for info in infos:
        title = info.xpath('div[2]/h4/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        author_id = re.findall(r'\d+', info.xpath('div[2]/p[1]/a[1]/@href')[0])[0]
        classes = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        bookid = info.xpath('div[1]/a/@data-bid')[0]
        state = info.xpath('div[2]/p[1]/span/text()')[0]
        ranking = info.xpath('div[1]/span/text()')[0]
        res.append(model(title=title, author=author, classes=classes,bookid=bookid, state=state, authorid=author_id, ranking=ranking))
    return res
