from crawling.helpers import *
from utils.date_helpers import subtract_days_from_date
from selenium import webdriver


class DataCrawler:
    def __init__(self, token_name):
        self.token_name = token_name

    def get_driver(self):
        token_name = self.token_name

        url = f"https://coinmarketcap.com/currencies/{token_name}/historical-data/"
        """
        Also, you can try to disable SSL verification by adding the following line of code before creating the webdriver instance. --ignore-ssl-errors=yes which tells the webdriver to ignore SSL errors when connecting to websites. --ignore-certificate-errors which tells the webdriver to ignore certificate errors when connecting to websites. Please keep in mind that disabling SSL verification is not recommended and it should only be used as a last resort.
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        # Crawl without loading Images
        prefs = {'profile.managed_default_content_settings.images': 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # # try to handle ERROR:gpu_init.cc(523)] Passthrough is not supported, GL is disabled, ANGLE is
        # chrome_options.add_argument("--enable-webgl")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--enable-webgl-developer-extensions")
        # chrome_options.add_argument("--enable-webgl-draft-extensions")
        # #
        driver = webdriver.Chrome(executable_path="crawling/chromedriver.exe", chrome_options=chrome_options)  # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        driver.execute_script("window.scrollBy(0, 500)")
        return driver

    @staticmethod
    def crawl_data(driver, to_date):
        wait = WebDriverWait(driver, 10)
        # date range button
        date_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/span/button'
        element = wait.until(EC.element_to_be_clickable((By.XPATH, date_range_button_xpath)))
        element.click()

        # Select date
        from_date = subtract_days_from_date(to_date, 100)
        select_from_date_to_date(driver, from_date, to_date)

        # Click continue
        continue_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/span/button'
        element = driver.find_element_by_xpath(continue_button_xpath)
        element.click()

        return driver
