import constants as c
from data_processing.helpers import read_from_json, write_to_json, append_token_to_txt
from utils.date_helpers import convert_cmc_date_str_to_yyyymmdd, subtract_days_from_date
from utils.helpers import get_token_run_log_path, print_and_log

import os
import pandas as pd


class DataProcessor:
    def __init__(self, token_name):
        self.token_name = token_name
        self.token_run_log_path = get_token_run_log_path(token_name)
        # self.token_run_log_path = f"{c.PROCESSING_LOG_PATH}{token_name}_run_log.json"
        self.processing_data_path = f'{c.PROCESSING_DATA_PATH}{token_name}.csv'

    def write_data_to_csv(self, data, l_cols):
        # token_name = self.token_name
        token_run_log_path = self.token_run_log_path

        df = pd.DataFrame(data, columns=l_cols)  # Create a DataFrame from the list of data
        batch_size = df.shape[0] - 1  # header row is not included
        max_date = convert_cmc_date_str_to_yyyymmdd(df['Date'].iloc[0])
        min_date = convert_cmc_date_str_to_yyyymmdd(df['Date'].iloc[-1])
        import json

        # with open(token_run_log_path, "r") as f:
        #     token_run_log = json.load(f)
        token_run_log = read_from_json(token_run_log_path)

        # Append data to csv
        processing_data_path = self.processing_data_path
        if os.path.exists(processing_data_path):
            # If the file exists, append the DataFrame to it
            df.to_csv(processing_data_path, mode='a', header=False, index=False)
        else:
            # If the file does not exist, create it and write the DataFrame to it, log the max_date
            # TODO max_date đang được log theo thuật toán chạy từ to_date -> from_date ==> sửa/ xem có cần dùng max_date ko
            df.to_csv(processing_data_path, mode='w', header=True, index=False)
            token_run_log['max_date'] = max_date
        # try: except FileNotFoundError: # ==> if the file does not exist, data will still be written to csv without cols

        token_run_log["batch_dates"].append([max_date, min_date])
        token_run_log["min_date"] = min_date
        token_run_log['is_started'] = True
        # with open(token_run_log_path, "w") as f:
        #     json.dump(token_run_log, f)
        write_to_json(token_run_log, token_run_log_path)
        print_and_log(f"token_name={self.token_name}, [{min_date}, {max_date}] {batch_size} rows has been written to csv")

        if batch_size < 100:
            # log last_batch_size, update is_done
            token_run_log = read_from_json(token_run_log_path)
            token_run_log["last_batch_size"] = batch_size
            token_run_log["is_done"] = True
            write_to_json(token_run_log, token_run_log_path)

    def refresh_is_done(self):
        try:
            is_done = read_from_json(self.token_run_log_path)['is_done']
        except FileNotFoundError:
            token_run_log_schema_dic = {"is_started": False, "is_done": False, "is_error": False,
                                        "is_no_data": None, "is_wrong_url": None,
                                        "max_date": None, "min_date": None, "batch_dates": [],
                                        "run_time": [], "last_batch_size": None}
            write_to_json(token_run_log_schema_dic, self.token_run_log_path)
            is_done = False

        return is_done

    def refresh_to_date(self):
        token_run_log = read_from_json(self.token_run_log_path)
        is_started = token_run_log['is_started']
        if is_started:
            to_date = subtract_days_from_date(token_run_log['min_date'], 1)
        else:
            to_date = c.TO_DATE
        print_and_log(f"token_name={self.token_name} to_date={to_date}")
        return to_date

    # def update_list_done(self):
    #     # append token_name into l_error_tokens.txt / l_done_tokens.txt
    #     token_name = self.token_name
    #     token_run_log_path = self.token_run_log_path
    #     token_run_log = read_from_json(token_run_log_path)
    #     is_error = token_run_log["is_error"]
    #     if is_error:
    #         append_token_to_txt(token_name, c.L_ERROR_TOKENS_PATH)
    #     else:  # done
    #         append_token_to_txt(token_name, c.L_DONE_TOKENS_PATH)
    #         # move data and log file to data/04_output
    #         token_output_data_path = f"{c.OUTPUT_DATA_PATH}{token_name}.csv"
    #         token_output_log_path = f"{c.OUTPUT_LOG_PATH}{token_name}_run_log.json"
    #         import shutil
    #         shutil.move(self.processing_data_path, token_output_data_path)
    #         shutil.move(token_run_log_path, token_output_log_path)
    def update_list_done(self):
        # append token_name into l_error_tokens.txt / l_done_tokens.txt
        token_name = self.token_name
        token_run_log_path = self.token_run_log_path

        append_token_to_txt(token_name, c.L_DONE_TOKENS_PATH)
        # move data and log file to data/04_output
        token_output_data_path = f"{c.OUTPUT_DATA_PATH}{token_name}.csv"
        token_output_log_path = f"{c.OUTPUT_LOG_PATH}{token_name}_run_log.json"
        import shutil
        shutil.move(self.processing_data_path, token_output_data_path)
        shutil.move(token_run_log_path, token_output_log_path)

    def update_list_error_done(self):
        # append token_name into l_error_tokens.txt / l_done_tokens.txt
        token_name = self.token_name
        token_run_log_path = self.token_run_log_path
        token_run_log = read_from_json(token_run_log_path)
        is_error = token_run_log["is_error"]
        if is_error:
            append_token_to_txt(token_name, c.L_ERROR_TOKENS_PATH)
