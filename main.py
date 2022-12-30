from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from cmc_navigator.cmc_navigator_main import *
from data_crawler.data_crawler_main import *

import time

start = time.perf_counter()
# code to be measured goes here


# Set the URL for CoinMarketCap's MANA page
# url = 'https://coinmarketcap.com/currencies/decentraland/historical-data/'
url = 'https://coinmarketcap.com/currencies/ethereum/historical-data/'
to_date = 20221111


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.execute_script("window.scrollBy(0, 500)")


cmc_navigator = CmcNavigator(driver, to_date)
cmc_navigator.navigate_cmc()

data_crawler = DataCrawler(driver)
data_crawler.crawl()

end = time.perf_counter()
print(f"Elapsed time: {end - start:0.2f} seconds")