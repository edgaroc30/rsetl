from sqlalchemy_models import Item,Quarter,Month,Week
from utils import DatabaseConnection

class QueryDB:
    def __init__(self):
        self.connection = DatabaseConnection()
        self.session = self.connection.get_session()

    def get_all_items(self):
        return self.session.query(Item).all()
    
    def get_all_items_after(self,id):
        return self.session.query(Item).filter(Item.id >= id).all()

    def get_all_quarter(self):
        return self.session.query(Quarter).all()

    def get_all_month(self):
        return self.session.query(Month).all()

    def get_all_week(self):
        return self.session.query(Week).all()