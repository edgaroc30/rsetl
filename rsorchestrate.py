import logging
from rsupdate import UpdateDB
from rsbuddy import Rsbuddy
from rsquery import QueryDB
import time

class Orchest(UpdateDB,QueryDB):
    def __init__(self,  sleep = True, sleep_time = 1):
        super().__init__()
        self.sleep_time = sleep_time
        self.sleep = sleep

    def update_per_item(self,id):
        logging.debug('Updating for: '+ str(id))
        self.upsert_month_item(id)
        time.sleep(self.sleep_time)
        self.upsert_quarter_item(id)
        time.sleep(self.sleep_time)
        self.upsert_week_item(id)
        logging.debug('Finished updating for: '+ str(id) + ' while sleeping: ' + str(self.sleep_time) + 's')

    def update_item_list(self):
        self.update_item_list

    def update_all_items_alltime(self):
        items  = self.get_all_items()
        for count, item in enumerate(items, start=1):
            logging.info('Updating items '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            self.update_per_item(item.id)

    def update_all_items_alltime_after(self,id):
        items  = self.get_all_items_after(id)
        for count, item in enumerate(items, start=1):
            logging.info('Updating all '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            self.update_per_item(item.id)
    
    def update_all_items_week(self):
        items  = self.get_all_items()
        for count, item in enumerate(items, start=1):
            logging.info('Updating week '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            time.sleep(self.sleep_time)
            self.upsert_week_item(item.id)
    
    def update_all_items_week_after(self,id):
        items  = self.get_all_items_after(id)
        for count, item in enumerate(items, start=1):
            logging.info('Updating week '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            time.sleep(self.sleep_time)
            self.upsert_week_item(item.id)

    def update_all_items_month(self):
        items  = self.get_all_items()
        for count, item in enumerate(items, start=1):
            logging.info('Updating month '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            time.sleep(self.sleep_time)
            self.upsert_month_item(item.id)

    def update_all_items_month_after(self,id):
        items  = self.get_all_items_after(id)
        for count, item in enumerate(items, start=1):
            logging.info('Updating month '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            time.sleep(self.sleep_time)
            self.upsert_month_item(item.id)

    def update_all_items_quarter(self):
        items  = self.get_all_items()
        for count, item in enumerate(items, start=1):
            logging.info('Updating month '+item.name +' ID: '+str(item.id) +' Sleep time: ' + str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            time.sleep(self.sleep_time)
            self.upsert_quarter_item(item.id)

    def update_all_items_quarter_after(self,id):
        items  = self.get_all_items_after(id)
        for count, item in enumerate(items, start=1):
            logging.info('Updating month '+item.name  +' ID: '+str(item.id) +' Sleep time: '+str(self.sleep_time) + 's' + ' Number of items left: ' + str(len(items)-count))
            time.sleep(self.sleep_time)
            self.upsert_quarter_item(item.id)

    def create_all(self):
        self.update_item_list()
        self.update_all_items_month()
