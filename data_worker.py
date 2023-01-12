import constants as c
from data_processing.helpers import write_to_json, read_from_json, append_token_to_txt
from utils.helpers import subtract_days_from_date, date_batch_map


def crawl_single_token(token_name):
    from crawling import data_crawler, data_parser
    # from data_processing import data_processor
    from selenium import webdriver
    import os
    import json
    url = f"https://coinmarketcap.com/currencies/{token_name}/historical-data/"

    """
    is_done = data_processor.refresh_is_done()
    """
    token_run_log_path = f"{c.TEMP_PATH}{token_name}_run_log.json"
    if not os.path.exists(token_run_log_path):
        token_run_log_schema_dic = {"is_started": False, "is_done": False, "is_error": False, "max_date": None, "min_date": None, "batch_dates": [], "to_date": [], "run_time": [], "last_batch_size": None}
        write_to_json(token_run_log_schema_dic, token_run_log_path)
        is_done = False
    else:
        token_run_log = read_from_json(token_run_log_path)
        is_done = token_run_log['is_done']

    # while not os.path.exists(done_file_path):
    while not is_done:  # TODO: clear folder temp ở đầu chương trình, vì đã lọc qua url_list
        import time
        start_time = time.time()

        """
        to_date = data_processor.refresh_to_date()
        """
        token_run_log = read_from_json(token_run_log_path)
        is_started = token_run_log['is_started']
        if is_started:
            to_date = subtract_days_from_date(token_run_log['min_date'], 1)
        else:
            to_date = c.TO_DATE

        batch_no = date_batch_map[int(to_date)]
        print(f"----- token_name={token_name}  batch_no={batch_no}  to_date={to_date}")

        # TODO 3 dòng này nhé vàp crawler?, return driver rồi truyền vào parser
        """
        # crawler = data_crawler.DataCrawler(token_name)
        driver = crawler.crawl_data(to_date)
        
        # parser = data_parser.DataParser(token_name)
        data = parser.parse_data(driver)
        
        # data_processor = data_processing.DataProcessor(token_name)
        data_processor.write_data_to_csv(data)
        data_processor.log_batch()
        
        logger
        """
        driver = webdriver.Chrome("crawling/chromedriver.exe")  # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        crawler = data_crawler.DataCrawler(driver, to_date)
        crawler.crawl_data()
        parser = data_parser.DataParser(driver, token_name)
        parser.parse_data()
        driver.close()  # All windows related to driver instance will quit #TODO nhét vào parser


        """
        data_processor.write_data_to_csv(data)
        is_done = data_processor.log_run_time(start_time, end_time)
        """
        # log run_time
        end_time = time.time()
        run_time = end_time - start_time
        run_time = format(run_time, ".2f")
        token_run_log = read_from_json(token_run_log_path)
        token_run_log['run_time'].append(run_time)

        write_to_json(token_run_log, token_run_log_path)

        print(f"token_name={token_name}  batch_no={batch_no}  run_time: {run_time} seconds")

        # check if is_done
        is_done = token_run_log["is_done"]
        if is_done:
            break

    """
    data_processor.log_whole_token()
    """
    # append token_name into l_error_tokens.txt / l_done_tokens.txt
    token_run_log = read_from_json(token_run_log_path)
    is_error = token_run_log["is_error"]
    if is_error:
        append_token_to_txt(token_name, "l_error_tokens.txt")
    else:
        append_token_to_txt(token_name, "l_done_tokens.txt")

    print(f"FINISH ----- token_name={token_name}")
