from utils.helpers import get_token_run_log_path
from data_processing.helpers import write_to_json, read_from_json


class DataLogger:
    def __init__(self, token_name):
        self.token_name = token_name
        self.token_run_log_path = get_token_run_log_path(token_name)

    def log_batch_run_time(self, start_time, end_time, batch_no):
        # log run_time
        token_name = self.token_name
        token_run_log_path = self.token_run_log_path
        run_time = end_time - start_time
        run_time = format(run_time, ".2f")
        token_run_log = read_from_json(token_run_log_path)
        token_run_log['run_time'].append(run_time)

        write_to_json(token_run_log, token_run_log_path)

        print(f"token_name={token_name}  batch_no={batch_no}  run_time: {run_time} seconds")

        # check if is_done
        is_done = token_run_log["is_done"]

        return is_done
