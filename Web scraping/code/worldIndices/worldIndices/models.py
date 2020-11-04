import datetime
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Index(Base):
    __tablename__ = "Indices"

    date = Column(Date, primary_key=True)
    index = Column(String, primary_key=True)
    country = Column(String)
    last = Column(Float)
    high = Column(Float)
    low = Column(Float)
    changeTotal = Column(Float)


