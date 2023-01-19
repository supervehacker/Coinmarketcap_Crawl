from data_worker import *
from utils.helpers import *
# from data_processing.helpers import refresh_l_tokens
from data_master import *

sys.stdout = Logger("mylog.log")  # redirect print function to log file
# l_urls = ['moonstarter', 'bunnypark', 'aptoslaunch-token', 'metaverse-vr', 'bikerush', 'smart-reward-token', 'bitica-coin', 'chronicum', 'blocknotex', 'drawshop-kingdom-reverse']
# l_urls = ['ruff', 'a', 'b']
# token_name = 'aptos'  # url_name #aptos bunnypark sportzchain ezcoin-market
# token_name = 'ruff'
# token_name = 'ethereum'
# l_tokens = data_master.refresh_l_tokens()
# dev
data_master = DataMaster()
l_tokens = data_master.refresh_l_tokens()

for token_name in l_tokens:
    data_worker = DataWorker(token_name)
    data_worker.crawl_single_token()
    break

# print(element.get_attribute('outerHTML'))
#
# import time
# time.sleep(10)
# import sys
# sys.exit()
