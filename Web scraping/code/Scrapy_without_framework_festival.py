import datetime
import logging
# scrapy api
import scrapy
from scrapy.crawler import CrawlerProcess
# sql conn
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, Date, DateTime, Float, Boolean, Text)

# CONNECTION TO DATABASE
Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine('sqlite:///Festivals.sqlite')


def create_table(engine):
    Base.metadata.create_all(bind=engine)


class Festival(Base):
    __tablename__ = "Festivals"
    date_scraped = Column(String, primary_key=True)
    name = Column(String, primary_key=True)
    date_begin = Column(String)
    date_end = Column(String)
    duration_in_days = Column(String)
    where = Column(String)
    genre = Column(String)
    city = Column(String)
    visitors = Column(String)
    price = Column(String)


# ITEMS
class FestivalItem(scrapy.Item):
    date_scraped = scrapy.Field()
    name = scrapy.Field()
    date_year = scrapy.Field()
    date_begin = scrapy.Field()
    date_end = scrapy.Field()
    duration_in_days = scrapy.Field()
    where = scrapy.Field()
    genre = scrapy.Field()
    city = scrapy.Field()
    visitors = scrapy.Field()
    price = scrapy.Field()


# PIPELINES
class FestivalCleanPipeline(object):
    date = datetime.datetime.now().date().strftime("%Y.%m.%d")

    def process_item(self, item, spider):
        item["date_scraped"] = self.date
        item["name"] = str(item["name"]).replace("\n", "").strip()
        item["date_begin"] = str(item["date_begin"]).replace("\n", "").strip() + item["date_year"][6:]

        date_end = str(item["date_end"]).replace("\n", "").strip()
        if date_end == "None":
            item["date_end"] = str(item["date_end"]).replace("\n", "").strip()
        else:
            item["date_end"] = str(item["date_end"]).replace("\n", "").strip() + item["date_year"][6:]

        item["duration_in_days"] = str(item["duration_in_days"]).replace("\n", "").replace("Tage", "").replace("Tag", "").strip()

        item["where"] = str(item["where"]).replace("\n", "").strip()
        item["genre"] = str(item["genre"]).replace("\n", "").strip()
        item["city"] = str(item["city"]).replace("\n", "").strip()

        visitors = str(item["visitors"]).replace("\n", "").strip()
        if visitors == "keine Daten":
            item["visitors"] = "None"
        else:
            item["visitors"] = str(item["visitors"]).replace("\n", "").strip()

        price = str(item["price"]).replace("\n", "").strip()
        if price == "n.v.":
            item["price"] = "None"
        else:
            item["price"] = str(item["price"]).replace("\n", "").strip()

        return item


class FestivalPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        self.engine = db_connect()
        create_table(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        festival = Festival()
        festival.date_scraped = item["date_scraped"]
        festival.name = item["name"]
        festival.date_begin = item["date_begin"]
        festival.date_end = item["date_end"]
        festival.duration_in_days = item["duration_in_days"]
        festival.where = item["where"]
        festival.genre = item["genre"]
        festival.city = item["city"]
        festival.visitors = item["visitors"]
        festival.price = item["price"]

        exists = session.query(
            session.query(Festival).filter_by(name=festival.name).filter_by(date_scraped=festival.date_scraped).exists()
        ).scalar()
        if exists is False:
            try:
                session.add(festival)
                session.commit()

            except:
                session.rollback()
                raise

            finally:
                session.close()

        return item


# SPIDER
class FestivalSpider(scrapy.Spider):
    name = "festival"
    year = int(datetime.datetime.now().date().strftime("%Y"))
    start_urls = [
        "https://www.festival-alarm.com/festival/region/Germany/" + str(year) + "/DE",
        "https://www.festival-alarm.com/festival/region/Germany/" + str(year + 1) + "/DE"
    ]
    allowed_domains = ["festival-alarm.com"]

    def parse(self, response):
        for festival in response.xpath('//tbody/tr'):
            festival_item = FestivalItem()
            festival_item["name"] = festival.xpath("td[1]/a[1]/text()").get()
            festival_item["date_year"] = festival.xpath("//thead/tr[1]/th[2]/text()").get()
            festival_item["date_begin"] = festival.xpath("td[2]/span[1]/text()").get()
            festival_item["date_end"] = festival.xpath("td[2]/span[2]/text()").get()
            festival_item["duration_in_days"] = festival.xpath("td[3]/text()").get()
            festival_item["where"] = festival.xpath("td[4]/text()").get()
            festival_item["genre"] = festival.xpath("td[6]/text()").get()
            festival_item["city"] = festival.xpath("td[7]/text()").get()
            festival_item["visitors"] = festival.xpath("td[9]/text()").get()
            festival_item["price"] = festival.xpath("td[10]/text()").get()

            yield festival_item


# run spider
if __name__ == "__main__":
    process = CrawlerProcess({
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/60.0.3112.101 Safari/537.36",
        "ROBOTSTXT_OBEY": True,
        "ITEM_PIPELINES": {"Scrapy_without_framework_festival.FestivalCleanPipeline": 200,
                           "Scrapy_without_framework_festival.FestivalPipeline": 300
                           }
    })
    process.crawl(FestivalSpider)
    process.start()
