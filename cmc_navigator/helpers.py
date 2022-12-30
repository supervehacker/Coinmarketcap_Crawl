from datetime import datetime, timedelta


def subtract_days_from_date(yyyymmdd, days):
    # Convert the input to a datetime object
    if isinstance(yyyymmdd, str):
        date = datetime.strptime(yyyymmdd, '%Y%m%d')
    elif isinstance(yyyymmdd, int):
        date = datetime.strptime(str(yyyymmdd), '%Y%m%d')
    else:
        raise ValueError("Invalid date format")

    # Subtract the specified number of days from the date
    result_date = date - timedelta(days=days)

    # Return the resulting date in the format "YYYYMMDD"
    return result_date.strftime('%Y%m%d')


def get_date_text_values(yyyymmdd):
    # Import the datetime module

    if isinstance(yyyymmdd, str):
        # Convert the input to a datetime object
        date = datetime.strptime(yyyymmdd, '%Y%m%d')
    elif isinstance(yyyymmdd, int):
        # Convert the input to a string and then to a datetime object
        date = datetime.strptime(str(yyyymmdd), '%Y%m%d')
    else:
        raise ValueError("Invalid date format")

    # Get the year, month, and date as separate values
    year_text_value = str(date.year)
    month_text_value = date.strftime("%b")  # "Feb" for February, etc.
    date_text_value = str(date.day).zfill(2)  # "20" instead of "20"

    return year_text_value, month_text_value, date_text_value


def date_select(driver, date):
    # driver = self.driver
    # from_date = self.from_date
    # to_date = self.to_date
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)

    # custom range button
    custom_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]'
    element = wait.until(EC.element_to_be_clickable((By.XPATH, custom_range_button_xpath)))
    element.click()
    element.click()

    year_text_value, month_text_value, date_text_value = get_date_text_values(date)
    # 1. YEAR
    # parrent_element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]')
    # wait = WebDriverWait(parrent_element, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[text()="{year_text_value}"]')))
    element.click()

    # 2. MONTH
    # parrent_element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[1]')
    # wait = WebDriverWait(parrent_element, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[text()="{month_text_value}"]')))
    element.click()  # Click the element

    # 3. DATE
    # parrent_element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[2]')
    # wait = WebDriverWait(parrent_element, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[text()="{date_text_value}"]')))
    element.click()  # Click the element


    # # custom range button
    # custom_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]'
    # element = wait.until(EC.element_to_be_clickable((By.XPATH, custom_range_button_xpath)))
    # element.click()
    # element.click()
