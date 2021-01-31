from app import db, app
import time
import click
from app.script.collection import collections
from app.script.monthlyticket import monthlytickets
from app.script.status24hourhot import hotsales
from app.script.readindex import readindexs
from app.script.recom import recoms
from app.script.signnew import signnews
from app.script.pubnew import pubnews
from app.script.fengyun import fengyuns
from app.models import QidianCollectionRank,QidianMonthlyTicketRank,Qidian24HourHotRank,QidianReadIndex, QidianRecom,QidianSignNew,QidianPubNew,QidianFengYun


@app.cli.command()
@click.option("--drop", is_flag=True)
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("OK!")


@app.cli.command()
def collection():
    QidianCollectionRank.query.delete()
    start = time.time()
    urls = ['https://www.qidian.com/rank/collect?page={}'.format(i) for i in range(1, 6)]
    for url in urls:
        collections(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def monthlyticket():
    QidianMonthlyTicketRank.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/yuepiao?page={i}' for i in range(1,6)]
    for url in urls:
        monthlytickets(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def status24hour():
    Qidian24HourHotRank.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/hotsales?page={i}' for i in range(1, 6)]
    for url in urls:
        hotsales(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def readindex():
    QidianReadIndex.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/readIndex?page={i}' for i in range(1,6)]
    for url in urls:
        readindexs(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def recom():
    QidianRecom.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/recom?page={i}' for i in range(1,6)]
    for url in urls:
        recoms(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def signnew():
    QidianSignNew.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/signnewbook?page={i}' for i in range(1,6)]
    for url in urls:
        signnews(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def pubnew():
    QidianPubNew.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/pubnewbook?page={i}' for i in range(1,6)]
    for url in urls:
        pubnews(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def fengyun():
    QidianFengYun.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/fengyun?page={i}' for i in range(1,6)]
    for url in urls:
        fengyuns(url)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")
