import requests
import logging

class Rsbuddy():

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'} # Random User Agent for API Crawler = realpart
        self.names_list =  'https://rsbuddy.com/exchange/names.json' # The id is the item_id used in the Quarter/Week/Month Graph calls
        self.summary_list = 'https://rsbuddy.com/exchange/summary.json' # This is the current price of all the items
        self.base_url = 'https://rsbuddy.com/exchange/graphs/{0}/{1}.json'
        self.quarter = 4320
        self.week = 180
        self.month = 1440

    def get_names(self):
        logging.debug('Getting names data from: '+ self.names_list)
        return self.request(self.names_list)

    def get_quarter_data(self, id):
        base_url = self.base_url.format(self.quarter,id)
        logging.debug('Getting quarter data from: ' + base_url)
        return self.request(base_url)    

    def get_week_data(self, id):
        base_url = self.base_url.format(self.week,id)
        logging.debug('Getting week data from: ' + base_url)
        return self.request(base_url)

    def get_month_data(self, id):
        base_url = self.base_url.format(self.month,id)
        logging.debug('Getting month data from: ' + base_url)
        return self.request(base_url)
    
    def request(self, url):
        try:
            r = requests.get(url, self.headers)
            if r.status_code >= 200 and r.status_code < 300:
                return r.json()
            else:
                logging.error('API Request returned status code: ' + str(r.status_code) + '\n URL Requested: ' + url)
                return None
        except Exception as e:
            logging.error('Failed during requesting: ' + url + 'Exception \n' + e)