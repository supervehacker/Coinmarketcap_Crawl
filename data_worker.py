from utils.helpers import print_and_log


class DataWorker:
    def __init__(self, token_name):
        self.token_name = token_name

    def crawl_single_token(self):
        from crawling import data_crawler, data_parser
        from data_processing import data_processor, data_logger
        from selenium.common.exceptions import TimeoutException

        token_name = self.token_name
        crawler = data_crawler.DataCrawler(token_name)
        parser = data_parser.DataParser(token_name)
        data_processor = data_processor.DataProcessor(token_name)

        is_done = data_processor.refresh_is_done()

        # TODO close the driver after x number of iterations

        while not is_done:
            import time
            start_time = time.time()

            driver = crawler.get_driver()
            to_date = data_processor.refresh_to_date()

            data_logger = data_logger.DataLogger(token_name, to_date)
            # batch_no = date_batch_map[int(to_date)]
            # print_and_log(f"----- token_name={token_name}  batch_no={batch_no}  to_date={to_date}")

            try:
                crawler.crawl_data(driver, to_date)
                data, l_cols = parser.parse_data(driver)
                if (data, l_cols) == (None, None):  # Handle cases with no_data
                    data_logger.log_no_data()

                    return
                else:
                    data_processor.write_data_to_csv(data, l_cols)  # TODO data_processor.write_data_to_csv(data)
            except TimeoutException:
                # crawl_error = crawler.check_wrong_url()
                # if crawl_error == 'x": data_logger.log_wrong_url()
                break

            end_time = time.time()

            is_done = data_logger.log_run_time_check_is_done(start_time, end_time)

            if is_done:
                break

            # driver.close()
            driver.quit()
        # append token_name into l_error_tokens.txt / l_done_tokens.txt
        data_processor.update_list_error_done()

        print_and_log(f"FINISH ----- token_name={token_name}")

    # def crawl_single_token_not_close_driver(self):
    #     from crawling import data_crawler, data_parser
    #     from data_processing import data_processor, data_logger
    #
    #     token_name = self.token_name
    #     crawler = data_crawler.DataCrawler(token_name)
    #     parser = data_parser.DataParser(token_name)
    #     data_processor = data_processor.DataProcessor(token_name)
    #     data_logger = data_logger.DataLogger(token_name)
    #
    #     is_done = data_processor.refresh_is_done()
    #
    #     # TODO close the driver after x number of iterations
    #     driver = crawler.get_driver()
    #     while not is_done:
    #         import time
    #         start_time = time.perf_counter()
    #         to_date = data_processor.refresh_to_date()
    #         batch_no = date_batch_map[int(to_date)]
    #         print_and_log(f"----- token_name={token_name}  batch_no={batch_no}  to_date={to_date}")
    #
    #         driver = crawler.crawl_data(driver, to_date)
    #         data, l_cols = parser.parse_data(driver)
    #         data_processor.write_data_to_csv(data, l_cols)  # TODO data_processor.write_data_to_csv(data)
    #
    #         end_time = time.perf_counter()
    #
    #         is_done = data_logger.log_batch_run_time(start_time, end_time, batch_no)
    #         if is_done:
    #             break
    #
    #     # driver.close()
    #     driver.quit()
    #     # append token_name into l_error_tokens.txt / l_done_tokens.txt
    #     data_processor.update_list_error_done()
    #
    #     print_and_log(f"FINISH ----- token_name={token_name}")
