from app import db, app
import click
from app.script.collection import collections
from queue import Queue
from threading import Thread


@app.cli.command()
@click.option("--drop", is_flag=True)
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("OK!")


@app.cli.command()
def collection():
    urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1, 6)]
    in_q = Queue()
    for u in urls:
        in_q.put(u)
    for _ in range(10):
        thread = Thread(target=collections, args=(in_q,))
        thread.daemon = True
        thread.start()
    in_q.join()
    click.echo("Spider OK!")
