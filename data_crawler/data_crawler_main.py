# import time
import pandas as pd

# from data_crawler.helpers import *


class DataCrawler:
    def __init__(self, driver):
        self.driver = driver

    def crawl(self):
        driver = self.driver
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC

        table_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table'
        # Wait for the table to not contain the text "Loading data..."
        WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((By.XPATH, table_xpath), 'Loading data...'))

        # Find the table element
        table_element = driver.find_element_by_xpath(table_xpath)
        # html = table_element.get_attribute('outerHTML')
        # print('table:')
        # print(html)

        # Scrape the data from the table
        data = []

        rows = table_element.find_elements_by_xpath('.//tbody/tr')
        for row in rows:
            # html = row.get_attribute('outerHTML')
            # print("row:")
            # print(html)
            cells = row.find_elements_by_xpath('.//td')
            data.append([cell.text for cell in cells])

        """
        Non-concurrent
        Elapsed time: 25.643122 seconds
        Elapsed time: 25.752819 seconds
        Elapsed time: 23.331920 seconds
        
        Concurrent
        Elapsed time: 21.973439 seconds
        Elapsed time: 23.189889 seconds
        Elapsed time: 21.862326 seconds
        """

        # import concurrent.futures
        #
        # def get_cell_text(row):
        #     cells = row.find_elements_by_xpath('.//td')
        #     return [cell.text for cell in cells]
        #
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     rows = table_element.find_elements_by_xpath('.//tbody/tr')
        #     results = [executor.submit(get_cell_text, row) for row in rows]
        #     for f in concurrent.futures.as_completed(results):
        #         data.append(f.result())

        # Create a DataFrame from the list of data
        df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Volume", "Market Cap"])
        # Print the DataFrame
        print(df)
