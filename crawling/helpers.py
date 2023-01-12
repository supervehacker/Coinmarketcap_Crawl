from utils.helpers import *


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
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    wait = WebDriverWait(driver, 10)
    custom_range_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]'
    element = wait.until(EC.element_to_be_clickable((By.XPATH, custom_range_button_xpath)))
    element.click()
    element.click()


def date_select(driver, date):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)

    year_text_value, month_text_value, date_text_value = get_date_text_values(date)

    # 1. YEAR
    # Note: nếu year = 2016, driver will click on "2016-2027" button ==> tìm giải pháp để tìm chính xác text của element đó, ko phải contain nữa

    yearpicker = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='yearpicker show']"))) # Wait for the div element with class "yearpicker show" to appear

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


def write_data_to_csv(token_name, data, l_cols):
    import pandas as pd
    df = pd.DataFrame(data, columns=l_cols)  # Create a DataFrame from the list of data

    batch_size = df.shape[0]
    max_date = convert_cmc_date_str_to_yyyymmdd(df['Date'].iloc[0])
    min_date = convert_cmc_date_str_to_yyyymmdd(df['Date'].iloc[-1])
    import json
    token_run_log_path = f"{c.TEMP_PATH}{token_name}_run_log.json"
    with open(token_run_log_path, "r") as f:
        token_run_log = json.load(f)

    # Append data to csv
    # Check if the file exists
    import os
    csv_path = f'{c.DATA_PATH}{token_name}.csv'
    if os.path.exists(csv_path):
        # If the file exists, append the DataFrame to it
        df.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        # If the file does not exist, create it and write the DataFrame to it, log the max_date
        df.to_csv(csv_path, mode='w', header=True, index=False)
        token_run_log['max_date'] = max_date

    token_run_log["batch_dates"].append([max_date, min_date])
    token_run_log["min_date"] = min_date
    token_run_log['is_started'] = True

    with open(token_run_log_path, "w") as f:
        json.dump(token_run_log, f)

    if batch_size < 100:
        # log last_batch_size, update is_done
        token_run_log = read_from_json(token_run_log_path)
        token_run_log["last_batch_size"] = batch_size
        token_run_log["is_done"] = True
        write_to_json(token_run_log, token_run_log_path)



