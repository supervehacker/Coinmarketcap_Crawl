from utils.date_helpers import get_date_text_values
from utils.helpers import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# CRAWLING HELPERS
def transform_date_picker(yyyymmdd: int) -> str:
    # Convert the integer to a date object
    date = datetime.strptime(str(yyyymmdd), '%Y%m%d')

    # Get the day of the month as an integer
    day = int(date.strftime('%d').lstrip('0'))

    # Determine the suffix for the day of the month
    if day in [1, 21, 31]:
        suffix = 'st'
    elif day in [2, 22]:
        suffix = 'nd'
    elif day in [3, 23]:
        suffix = 'rd'
    else:
        suffix = 'th'

    # Format the date as a string
    return f"Choose {date.strftime('%A')}, {date.strftime('%B')} {day}{suffix}, {date.strftime('%Y')}"
# for yyyymmdd in [20220311, 20220312, 20220313, 20220321, 20220322, 20220323, 20220324, 20220331]:
#     print(yyyymmdd, transform_date_picker(yyyymmdd))


def custom_range_button_double_click(driver):
    wait = WebDriverWait(driver, 10)
    custom_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]'
    element = wait.until(EC.element_to_be_clickable((By.XPATH, custom_range_button_xpath)))
    element.click()
    element.click()


def date_select(driver, date):
    wait = WebDriverWait(driver, 10)

    year_text_value, month_text_value, date_text_value = get_date_text_values(date)

    # 1. YEAR
    # Note: nếu year = 2016, driver will click on "2016-2027" button ==> tìm giải pháp để tìm chính xác text của element đó, ko phải contain nữa
    yearpicker = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='yearpicker show']")))  # Wait for the div element with class "yearpicker show" to appear

    # element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[text()="{year_text_value}"]')))
    # If you start an XPath expression with //, it begins searching from the root of document. To search relative to a particular element, you should prepend the expression with . instead:
    element = WebDriverWait(yearpicker, 10).until(EC.element_to_be_clickable((By.XPATH, f'.//span[text()="{year_text_value}"]')))
    # element = yearpicker.find_element_by_xpath(f".//span[text()='{year_text_value}']")
    element.click()

    # 2. MONTH
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[text()="{month_text_value}"]')))
    element.click()

    # 3. DATE
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[aria-label="{transform_date_picker(date)}"]')))
    # element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{date_text_value}"]')))
    element.click()


def select_from_date_to_date(driver, from_date, to_date):
    wait = WebDriverWait(driver, 10)

    custom_range_button_double_click(driver)
    try:
        if from_date <= 20151231:  # from_date <= 2015 (phải sang trang mới)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'icon-Chevron-left')]")))  # click sang trái
            element.click()
        date_select(driver, from_date)
    except TimeoutException:
        date_select(driver, from_date)
    custom_range_button_double_click(driver)
    date_select(driver, to_date)
