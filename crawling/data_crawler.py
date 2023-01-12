from crawling.helpers import *


class DateSelector:
    def __init__(self, driver, from_date, to_date):
        self.driver = driver
        self.from_date = from_date
        self.to_date = to_date

    def select_from_date_to_date(self):
        driver = self.driver
        from_date = self.from_date
        to_date = self.to_date
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        # TODO to_date ~ 2016 ~ from_date > 2015 (phải sang trang mới)
        wait = WebDriverWait(driver, 10)

        custom_range_button_double_click(driver)

        if from_date <= 20151231:  # from_date <= 2015 (phải sang trang mới)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'icon-Chevron-left')]")))  # click sang trái
            element.click()

        date_select(driver, from_date)

        custom_range_button_double_click(driver)

        date_select(driver, to_date)


class DataCrawler:
    def __init__(self, driver, to_date):
        self.driver = driver
        # self.url = url
        self.to_date = to_date

    def crawl_data(self):

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # url = self.url
        to_date = self.to_date
        from_date = subtract_days_from_date(to_date, 100)

        driver = self.driver

        driver.execute_script("window.scrollBy(0, 500)")
        wait = WebDriverWait(driver, 10)

        # date range button
        date_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/span/button'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, date_range_button_xpath)))
        element.click()

        # Select date
        date_selector = DateSelector(driver, from_date, to_date)  # TODO remove DateSelector class
        date_selector.select_from_date_to_date()

        # Click continue
        continue_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/span/button'
        element = driver.find_element_by_xpath(continue_button_xpath)
        element.click()
