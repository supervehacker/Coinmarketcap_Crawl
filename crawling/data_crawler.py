from crawling.helpers import *
# from utils.helpers import print_and_log

from selenium import webdriver


class DataCrawler:
    def __init__(self, token_name):
        self.token_name = token_name
        self.url = url = f"https://coinmarketcap.com/currencies/{token_name}/historical-data/"

    def get_driver(self):
        options = webdriver.ChromeOptions()
        """
        Also, you can try to disable SSL verification by adding the following line of code before creating the webdriver instance. --ignore-ssl-errors=yes which tells the webdriver to ignore SSL errors when connecting to websites. --ignore-certificate-errors which tells the webdriver to ignore certificate errors when connecting to websites. Please keep in mind that disabling SSL verification is not recommended and it should only be used as a last resort.
        """
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        # Crawl without loading Images
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        # # try to handle ERROR:gpu_init.cc(523)] Passthrough is not supported, GL is disabled, ANGLE is
        # chrome_options.add_argument("--enable-webgl")
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--enable-webgl-developer-extensions")
        # chrome_options.add_argument("--enable-webgl-draft-extensions")
        # #
        """
        When using Selenium with Chrome, you can prevent the browser from popping up on your screen by using the "headless" mode. In headless mode, the browser runs in the background without displaying any UI.
        """
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path="crawling/chromedriver.exe", chrome_options=options)   # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)
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
        from utils.date_helpers import subtract_days_from_date
        from_date = subtract_days_from_date(to_date, 100)
        select_from_date_to_date(driver, from_date, to_date)

        # Click continue
        continue_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/span/button'
        element = driver.find_element_by_xpath(continue_button_xpath)
        element.click()

    def is_url_redirected(self, driver):
        orig_url = self.url
        curr_url = driver.current_url
        if orig_url != curr_url:  # token_name = 'golem' ~ url has been redirected
            orig_url_curr_url_str = f"{orig_url} {curr_url}"
            print_and_log(f"url was redirected: {orig_url_curr_url_str}")
            from data_processing.helpers import append_element_to_txt
            append_element_to_txt(f"{orig_url_curr_url_str}", f"{c.PROCESSING_ERROR_LOG_PATH}/1_redirected_urls.txt")
            return True
        else:
            return False

    def is_url_not_exist(self, driver):
        """token_name = 'terra-classic'
        Sorry, we couldn't find your page"""
        err_msg_xpath = "/html/body/div/div/div[1]/div/div[1]/p[2]"
        err_element = driver.find_element_by_xpath(err_msg_xpath)
        if err_element.text == "Sorry, we couldn't find your page":
            # url_not_exists = True
            print_and_log(f"url does not exist: {self.url} -- ")
            return True
        else:
            return False

    def save_current_screenshot(self, driver):
        from utils.date_helpers import current_time_formatted_str
        driver.save_screenshot(f"{c.PROCESSING_ERROR_LOG_PATH}{self.token_name}-{current_time_formatted_str()}.png")
        print_and_log(f"-----Screenshot saved token_name={self.token_name} TimeoutException has not been handled")

