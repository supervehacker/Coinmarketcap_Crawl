from utils.helpers import print_and_log


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
            data_logger = DataLogger(token_name, to_date)
            try:
                crawler.crawl_data(driver, to_date)
            except TimeoutException:
                # print exception
                # crawl_error = crawler.check_wrong_url()
                # if crawl_error == 'x": data_logger.log_wrong_url()
                driver.quit()
                break

            data, l_cols = parser.parse_data(driver)
            driver.quit()

            if (data, l_cols) == (None, None):  # Handle cases with no_data
                data_logger.log_no_data()
                return
            else:
                token_run_log, batch_size = data_processor.write_data_to_csv(data, l_cols)  # TODO data_processor.write_data_to_csv(data)
                if batch_size < 100:
                    # log last_batch_size, is_done
                    token_run_log["last_batch_size"] = batch_size
                    token_run_log["is_done"] = True
                    is_done = True

            end_time = time.time()
            run_time = format(end_time - start_time, ".2f")
            token_run_log['run_time'].append(run_time)
            print_and_log(f"------done batch token_name={token_name} to_date={to_date} run_time: {run_time} seconds")
            # is_done = data_logger.log_run_time_check_is_done(start_time, end_time)

            data_logger.write_token_run_log(token_run_log)

            if is_done:
                data_processor.move_done_files()
                print_and_log(f"FINISH ----- token_name={token_name}")
                break

        # append token_name into l_error_tokens.txt / l_done_tokens.txt



    # def crawl_single_token_not_close_driver(self):
