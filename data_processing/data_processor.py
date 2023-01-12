import constants as c
from data_processing.helpers import read_from_json, write_to_json, append_token_to_txt
from utils.date_helpers import convert_cmc_date_str_to_yyyymmdd, subtract_days_from_date
from utils.helpers import get_token_run_log_path

import os
import pandas as pd


class DataProcessor:
    def __init__(self, token_name):
        self.token_name = token_name
        self.token_run_log_path = get_token_run_log_path(token_name)

    def write_data_to_csv(self, data, l_cols):
        token_name = self.token_name
        token_run_log_path = self.token_run_log_path

        if (data, l_cols) == (None, None):  # Handle cases with no_data
            print(f"token_name=token_name --- No data is available now")
            return

        df = pd.DataFrame(data, columns=l_cols)  # Create a DataFrame from the list of data
        batch_size = df.shape[0]
        max_date = convert_cmc_date_str_to_yyyymmdd(df['Date'].iloc[0])
        min_date = convert_cmc_date_str_to_yyyymmdd(df['Date'].iloc[-1])
        import json

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

    def refresh_is_done(self):
        token_run_log_path = self.token_run_log_path
        if not os.path.exists(token_run_log_path):
            token_run_log_schema_dic = {"is_started": False, "is_done": False, "is_error": False, "max_date": None,
                                        "min_date": None, "batch_dates": [],
                                        # "to_date": [],
                                        "run_time": [], "last_batch_size": None}
            write_to_json(token_run_log_schema_dic, token_run_log_path)
            is_done = False
        else:
            token_run_log = read_from_json(token_run_log_path)
            return token_run_log['is_done']

    def refresh_to_date(self):
        token_run_log_path = self.token_run_log_path
        token_run_log = read_from_json(token_run_log_path)
        is_started = token_run_log['is_started']
        if is_started:
            to_date = subtract_days_from_date(token_run_log['min_date'], 1)
        else:
            to_date = c.TO_DATE

        return to_date

    def update_list_error_done(self):
        # append token_name into l_error_tokens.txt / l_done_tokens.txt
        token_name = self.token_name
        token_run_log_path = self.token_run_log_path
        token_run_log = read_from_json(token_run_log_path)
        is_error = token_run_log["is_error"]
        if is_error:
            append_token_to_txt(token_name, "l_error_tokens.txt")
        else:
            append_token_to_txt(token_name, "l_done_tokens.txt")

