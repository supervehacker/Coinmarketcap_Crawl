from cmc_navigator.helpers import *


class DateSelector:
    def __init__(self, driver, from_date, to_date):
        self.driver = driver
        self.from_date = from_date
        self.to_date = to_date

    def select_from_date_to_date(self):
        driver = self.driver
        from_date = self.from_date
        to_date = self.to_date
        date_select(driver, from_date)
        date_select(driver, to_date)


class CmcNavigator:
    def __init__(self, driver, to_date):
        self.driver = driver
        # self.url = url
        self.to_date = to_date

    def navigate_cmc(self):

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # url = self.url
        to_date = self.to_date
        from_date = subtract_days_from_date(to_date, 200)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver

        wait = WebDriverWait(driver, 10)

        # date range button
        date_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/span/button'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, date_range_button_xpath)))
        element.click()

        # # custom range button
        # custom_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]'
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, custom_range_button_xpath)))
        # element.click()
        # element.click()

        # Select date
        date_selector = DateSelector(driver, from_date, to_date)
        date_selector.select_from_date_to_date()

        # Click continue
        continue_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/span/button'
        element = driver.find_element_by_xpath(continue_button_xpath)
        element.click()
