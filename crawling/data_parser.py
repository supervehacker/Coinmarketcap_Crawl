from crawling.helpers import *


class DataParser:
    def __init__(self, token_name):
        self.token_name = token_name

    def parse_data(self, driver):
        token_name = self.token_name
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC

        table_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[2]/table'
        # Wait for the table to not contain the text "Loading data..."
        WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((By.XPATH, table_xpath), 'Loading data...'))

        # Find the table element
        table_element = driver.find_element_by_xpath(table_xpath)
        # Scrape the data from the table
        data = []
        rows = table_element.find_elements_by_xpath('.//tbody/tr')
        # print(f"rows: {rows} ---- len = {len(rows)}")
        for row in rows:
            # print(row.get_attribute('outerHTML'))
            cells = row.find_elements_by_xpath('.//td')
            data.append([cell.text for cell in cells])

        if data[0][0] == 'No data is available now': # print(data)  # [['No data is available now']]
            print(f"token={token_name}, to_date ={c.TO_DATE}, 'No data is available now'")
            import json
            token_run_log_path = f"{c.TEMP_PATH}{token_name}_run_log.json"
            with open(token_run_log_path, "r") as f:
                token_run_log = json.load(f)
                token_run_log["is_done"] = True
                token_run_log["is_error"] = True
                with open(token_run_log_path, "w") as f:
                    json.dump(token_run_log, f)
            return None, None
        # import sys
        # sys.exit()

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

        thead = table_element.find_element_by_xpath('.//thead/tr')
        cells = thead.find_elements_by_xpath('.//th')
        l_cols = [cell.text for cell in cells]        # print(l_cols) ["Date", "Open", "High", "Low", "Close", "Volume", "Market Cap"]
        ## TODO append l_cols vào dòng đầu tiên của data => write_data_to_csv(data)
        driver.close()  # All windows related to driver instance will quit #TODO nhét vào parser

        # write_data_to_csv(token_name, data, l_cols)
        return data, l_cols

