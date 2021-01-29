from app import db, app
import time
import click
from app.script.collection import collections
from app.models import QidianModel


@app.cli.command()
@click.option("--drop", is_flag=True)
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("OK!")


@app.cli.command()
def collection():
    data = QidianModel.query.all()
    for d in data:
        db.session.delete(d)
    db.session.commit()
    start = time.time()
    urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1, 6)]
    for url in urls:
        collections(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")
