import data_processing.helpers
# from utils.helpers import print_and_log


class DataWorker:
    def __init__(self, token_name):
        self.token_name = token_name

    def crawl_single_token(self):
        from crawling import data_crawler, data_parser
        from data_processing import data_processor
        from selenium.common.exceptions import TimeoutException

        token_name = self.token_name
        crawler = data_crawler.DataCrawler(token_name)
        parser = data_parser.DataParser(token_name)
        data_processor = data_processor.DataProcessor(token_name)

        is_done = data_processor.refresh_is_done()

        while not is_done:
            from data_processing.data_logger import DataLogger
            import time
            start_time = time.time()

            driver = crawler.get_driver()
            to_date = data_processor.refresh_to_date()

            try:
                crawler.crawl_data(driver, to_date)
            except TimeoutException:
                if crawler.is_url_redirected(driver):
                    data_processor.delete_error_runlog_file_append_l_error()
                elif crawler.is_url_not_exist(driver):
                    data_processor.delete_error_runlog_file_append_l_error()
                else:
                    crawler.save_current_screenshot(driver)
                driver.quit()
                break

            data, l_cols = parser.parse_data(driver)
            driver.quit()

            data_logger = DataLogger(token_name, to_date)

            if (data, l_cols) == (None, None):  # Handle cases with no_data
                data_logger.log_no_data_error()
                data_processor.move_no_data_files_append_l_error()
                break
            else:
                token_run_log, batch_size = data_processor.write_data_to_csv(data, l_cols)  # TODO data_processor.write_data_to_csv(data)
                if batch_size < 100:
                    # log last_batch_size, is_done
                    token_run_log["last_batch_size"] = batch_size
                    token_run_log["is_done"] = True
                    is_done = True
                    data_processor.move_done_files_append_l_done()
                token_run_log = data_logger.append_run_time_to_run_log(token_run_log, start_time)
                data_logger.write_run_log_to_json(token_run_log)

            if is_done:  # TODO check if these 2 lines are needed? => no
                break

    #
    # def crawl_single_token_not_close_driver(self):
