from data_worker import crawl_single_token
from utils.helpers import *
from data_processing.helpers import refresh_l_tokens

sys.stdout = Logger("mylog.log")  # redirect print function to log file
# l_urls = ['moonstarter', 'bunnypark', 'aptoslaunch-token', 'metaverse-vr', 'bikerush', 'smart-reward-token', 'bitica-coin', 'chronicum', 'blocknotex', 'drawshop-kingdom-reverse']
# l_urls = ['ruff', 'a', 'b']
# token_name = 'aptos'  # url_name #aptos bunnypark sportzchain ezcoin-market
# token_name = 'ruff'
# token_name = 'ethereum'
# l_tokens = data_master.refresh_l_tokens()
# mainaa
l_tokens = refresh_l_tokens()

for token_name in l_tokens:
    crawl_single_token(token_name)
    break

# print(element.get_attribute('outerHTML'))
#
# import time
# time.sleep(10)
# import sys
# sys.exit()
