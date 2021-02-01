from app import db, app
import time
import click
from app.script.RankSpider import rankspider
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
        rankspider(url,QidianCollectionRank)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def monthlyticket():
    QidianMonthlyTicketRank.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/yuepiao?page={i}' for i in range(1,6)]
    for url in urls:
        rankspider(url,QidianMonthlyTicketRank)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def status24hour():
    Qidian24HourHotRank.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/hotsales?page={i}' for i in range(1, 6)]
    for url in urls:
        rankspider(url,Qidian24HourHotRank)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def readindex():
    QidianReadIndex.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/readIndex?page={i}' for i in range(1,6)]
    for url in urls:
        rankspider(url,QidianReadIndex)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def recom():
    QidianRecom.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/recom?page={i}' for i in range(1,6)]
    for url in urls:
        rankspider(url,QidianRecom)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def signnew():
    QidianSignNew.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/signnewbook?page={i}' for i in range(1,6)]
    for url in urls:
        rankspider(url,QidianSignNew)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def pubnew():
    QidianPubNew.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/pubnewbook?page={i}' for i in range(1,6)]
    for url in urls:
        rankspider(url,QidianPubNew)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")


@app.cli.command()
def fengyun():
    QidianFengYun.query.delete()
    start = time.time()
    urls = [f'https://www.qidian.com/rank/fengyun?page={i}' for i in range(1,6)]
    for url in urls:
        rankspider(url,QidianFengYun)
    end = time.time()
    click.echo(f"Spider OK! It takes {end - start:.2f} times!")
