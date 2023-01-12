from crawling.helpers import *
from utils.date_helpers import subtract_days_from_date
from selenium import webdriver


class DataCrawler:
    def __init__(self, token_name):
        self.token_name = token_name

    def crawl_data(self, to_date):
        token_name = self.token_name
        from_date = subtract_days_from_date(to_date, 100)
        url = f"https://coinmarketcap.com/currencies/{token_name}/historical-data/"

        driver = webdriver.Chrome("crawling/chromedriver.exe")  # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        driver.execute_script("window.scrollBy(0, 500)")
        wait = WebDriverWait(driver, 10)

        # date range button
        date_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/span/button'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, date_range_button_xpath)))
        element.click()

        # Select date
        # date_selector = DateSelector(driver, from_date, to_date)  # TODO remove DateSelector class
        # date_selector.select_from_date_to_date()
        select_from_date_to_date(driver, from_date, to_date)

        # Click continue
        continue_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/span/button'
        element = driver.find_element_by_xpath(continue_button_xpath)
        element.click()

        return driver
