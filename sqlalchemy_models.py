import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from utils import DatabaseConnection

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(250), nullable=False)
    store = Column(Integer, nullable=False)

class Quarter(Base):
    __tablename__ = 'quarter'
    id_item = Column(Integer, nullable=False, primary_key=True)
    timestamp = Column(DateTime, nullable=False, primary_key=True)
    overallPrice = Column(Integer, nullable=False)
    overallQuantity = Column(Integer, nullable=False)
    buyingPrice = Column(Integer, nullable=False)
    buyingQuantity = Column(Integer, nullable=False)
    sellingPrice = Column(Integer, nullable=False)
    sellingQuantity = Column(Integer, nullable=False)

class Week(Base):
    __tablename__ = 'week'
    id_item = Column(Integer, nullable=False, primary_key=True)
    timestamp = Column(DateTime, nullable=False, primary_key=True)
    overallPrice = Column(Integer, nullable=False)
    overallQuantity = Column(Integer, nullable=False)
    buyingPrice = Column(Integer, nullable=False)
    buyingQuantity = Column(Integer, nullable=False)
    sellingPrice = Column(Integer, nullable=False)
    sellingQuantity = Column(Integer, nullable=False)

class Month(Base):
    __tablename__ = 'month'
    id_item = Column(Integer, nullable=False, primary_key=True)
    timestamp = Column(DateTime, nullable=False, primary_key=True)
    overallPrice = Column(Integer, nullable=False)
    overallQuantity = Column(Integer, nullable=False)
    buyingPrice = Column(Integer, nullable=False)
    buyingQuantity = Column(Integer, nullable=False)
    sellingPrice = Column(Integer, nullable=False)
    sellingQuantity = Column(Integer, nullable=False)
 

db = DatabaseConnection()

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(db.engine)