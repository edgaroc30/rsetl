import logging
from rsbuddy import Rsbuddy
from sqlalchemy_models import Item,Quarter,Month, Week
from datetime import datetime
from utils import DatabaseConnection


class UpdateDB:
    def __init__(self):
        self.connection = DatabaseConnection()
        self.session = self.connection.get_session()
        self.rs = Rsbuddy()
    
    def upsert_items(self):
        item_list = list(self.rs.get_names().items())
        if item_list != None:
            for i in item_list:
                self.session.merge(Item(id=i[0],name=i[1]['name'],store=i[1]['store']))
            self.session.commit()
        else:
            logging.error('Empty item list')
    
    def upsert_quarter_item(self,id):
        quarter_list = self.rs.get_quarter_data(id)
        if quarter_list != None:
            for i in quarter_list:
                self.session.merge(Quarter(
                    id_item = id,
                    timestamp = datetime.fromtimestamp(i['ts']/1000),
                    overallPrice = i['overallPrice'],
                    overallQuantity = i['overallQuantity'],
                    buyingPrice = i['buyingPrice'],
                    buyingQuantity = i['buyingQuantity'],
                    sellingPrice = i['sellingPrice'],
                    sellingQuantity = i['sellingQuantity']))
            self.session.commit()
        else:
            logging.warning('Empty Quarter data for:' + str(id))
    
    def upsert_month_item(self,id):
        quarter_list = self.rs.get_month_data(id)
        if quarter_list != None:
            for i in quarter_list:
                self.session.merge(Month(
                    id_item = id,
                    timestamp = datetime.fromtimestamp(i['ts']/1000),
                    overallPrice = i['overallPrice'],
                    overallQuantity = i['overallQuantity'],
                    buyingPrice = i['buyingPrice'],
                    buyingQuantity = i['buyingQuantity'],
                    sellingPrice = i['sellingPrice'],
                    sellingQuantity = i['sellingQuantity']))
            self.session.commit()
        else:
            logging.warning('Empty Month data for: '+ str(id))
    
    def upsert_week_item(self,id):
        quarter_list = self.rs.get_week_data(id)
        if quarter_list!= None:
            for i in quarter_list:
                self.session.merge(Week(
                    id_item = id,
                    timestamp = datetime.fromtimestamp(i['ts']/1000),
                    overallPrice = i['overallPrice'],
                    overallQuantity = i['overallQuantity'],
                    buyingPrice = i['buyingPrice'],
                    buyingQuantity = i['buyingQuantity'],
                    sellingPrice = i['sellingPrice'],
                    sellingQuantity = i['sellingQuantity']))
            self.session.commit()
        else:
            logging.warning('Empty Week data for: '+ str(id))