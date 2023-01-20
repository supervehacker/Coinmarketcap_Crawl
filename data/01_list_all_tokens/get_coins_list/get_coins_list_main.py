from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from helpers import *

# https://coinmarketcap.com/historical/20230101/ 200 tokens/page ==> click Load More 9 times to get 2000 tokens
date_to_crawl = 20230101
url = f'https://coinmarketcap.com/historical/{date_to_crawl}'
# url = https://coinmarketcap.com/all/views/all/  # TODO edit to list url
# url = url + str(date_to_crawl)
print(url)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.execute_script("window.scrollBy(0, 500)")

# STEP 1: click "Load more" n times
no_click = 40
print(f"#STEP 1: Click 'Load more' {no_click} times")
tokens_list_navigator = TokensListNavigator(driver)
tokens_list_navigator.click_load_more(no_click=no_click)


# STEP 2: get all data in the table
print("#STEP 2: Get all data in the table")
tokens_list_crawler = TokensListCrawler(driver)
tokens_list_crawler.crawl()

## TODO sửa xuất csv thành append liên tục 50 dòng 1
