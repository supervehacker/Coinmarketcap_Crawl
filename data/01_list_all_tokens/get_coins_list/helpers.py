def beautify_str(string):
    # convert str to "aa_bb" format
    string = string.lower()
    string = string.replace(" ", "-")
    return string


class TokensListNavigator:
    def __init__(self, driver):
        self.driver = driver

    def click_load_more(self, no_click):
        driver = self.driver
        no_click = no_click
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        load_more_button_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div[3]/div[2]/button'
        wait = WebDriverWait(driver, 10)

        for i in range(no_click):  # Click n times
            element = wait.until(EC.element_to_be_clickable((By.XPATH, load_more_button_xpath)))
            driver.execute_script("arguments[0].click();",
                                  element)  # Another element is covering the element you are trying to click. You could use execute_script() to click on this.

        print(f"Load_more button is clicked {no_click} times")
        import time
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom
        driver.execute_script("window.scrollBy(0, -300)")  # scroll up 300px to see where we ate


class TokensListCrawler:
    def __init__(self, driver):
        self.driver = driver

    def crawl(self):
        import pandas as pd
        driver = self.driver

        table_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table'
        # Find the table element
        table_element = driver.find_element_by_xpath(table_xpath)

        # Scrape the data from the table
        # l_cols = ['rank', 'name', 'symbol', 'market_cap', 'price', 'circulating_supply', 'volume_(24h)', '%_1h', '%_24h', '%_7d', 'more']
        l_cols = ['rank', 'name', 'url_name']
        df_list_tokens = pd.DataFrame(columns=l_cols)
        df_list_tokens.to_csv('list_tokens.csv', index=False)

        rows = table_element.find_elements_by_xpath('.//tbody/tr')
        data = []
        for count, row in enumerate(rows):
            cells = row.find_elements_by_xpath('.//td')[:2] #get first 2 cols
            data.append([cell.text for cell in cells])
            if (count+1) % 100 == 0:
                df_list_tokens = pd.DataFrame(data, columns=l_cols)
                # df_csv = df_list_tokens.loc[:, ['rank', 'name', 'symbol', 'market_cap']]
                df_list_tokens['url_name'] = df_list_tokens['name'].map(lambda x: beautify_str(x))
                df_list_tokens.to_csv('list_tokens.csv', header=False, index=False, mode='a')  # append df to the csv without header and index
                data = []
                print(f"--crawled {count + 1} rows")

        print("list_tokens.csv is exported")

        # # Scrape the data from the table
        # data = []
        # rows = table_element.find_elements_by_xpath('.//tbody/tr')
        # for count, row in enumerate(rows):
        #     cells = row.find_elements_by_xpath('.//td')
        #     data.append([cell.text for cell in cells])
        #     if (count+1) % 50 == 0:
        #         print(f"--crawled {count+1} rows")
        #
        #
        #
        # l_cols = ['rank', 'name', 'symbol', 'market_cap', 'price', 'circulating_supply', 'volume_(24h)', '%_1h',
        #           '%_24h', '%_7d', 'more']
        # df_list_tokens = pd.DataFrame(data, columns=l_cols)
        # df_list_tokens = df_list_tokens[['rank', 'name', 'symbol', 'market_cap']]
        # df_list_tokens['url_name'] = df_list_tokens['name'].map(lambda x: beautify_str(x))
        #
        # df_list_tokens.to_csv('list_tokens.csv', index=False)
        #
        # print("list_tokens.csv is exported")

        # thead = table_element.find_element_by_xpath('.//thead/tr')
        # cells = thead.find_elements_by_xpath('.//th')
        # l = [cell.text for cell in cells]
        # # print(l) # l = ['Rank', 'Name', 'Symbol', 'Market Cap', 'Price', 'Circulating Supply', 'volume (24h)', '% 1h', '% 24h', '% 7d', '']
        # l_cols = []
        # for col in l:
        #     col = col.lower()
        #     col = col.replace(" ", "_")
        #     l_cols.append(col)
        # print(l_cols) #['rank', 'name', 'symbol', 'market_cap', 'price', 'circulating_supply', 'volume_(24h)', '%_1h', '%_24h', '%_7d', '']