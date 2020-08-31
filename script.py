import logging
from rsorchestrate import Rsbuddy
logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s %(lineno)d:%(message)s',
    datefmt='%Y/%m/%d %H:%M:%S ',
    filename='request.log',
    filemode='w',
    level=logging.INFO)

from rsorchestrate import Orchest 
from rsquery import QueryDB

test = Orchest()
test.update_all_items_quarter()