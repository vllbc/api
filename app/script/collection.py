from threading import Lock
lock = Lock()
import requests
from lxml import etree
from app import app,db
from app.models import QidianModel

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}


def collections(queues):
    while queues.empty() is not True:
        res = requests.get(queues.get(), headers=headers)
        sel = etree.HTML(res.text)
        infos = sel.xpath('//*[@id="rank-view-list"]/div/ul/li')
        for info in infos:
            title = info.xpath('div[2]/h4/a/text()')[0]
            author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
            classes = info.xpath('div[2]/p[1]/a[2]/text()')[0]
            lock.acquire()
            new_model = QidianModel(title=title, author=author, classes=classes)
            db.session.add(new_model)
            db.session.commit()
            lock.release()
        queues.task_done()
