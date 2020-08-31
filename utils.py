from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine('sqlite:///rsstorage.db')
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        
    def get_session(self):
        return self.session