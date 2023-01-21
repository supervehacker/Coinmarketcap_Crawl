from utils.helpers import get_token_run_log_path, print_and_log
from data_processing.helpers import write_to_json, read_from_json


class DataLogger:
    def __init__(self, token_name):
        self.token_name = token_name
        self.token_run_log_path = get_token_run_log_path(token_name)

    # def log_no_data(self):
    #     token_run_log = read_from_json(self.token_run_log_path)
    #     token_run_log['is_no_data'] = True
    #     write_to_json(token_run_log, self.token_run_log_path)
    #
    # def log_wrong_url(self):
    #     token_run_log = read_from_json(self.token_run_log_path)
    #     token_run_log['is_wrong_url'] = True
    #     write_to_json(token_run_log, self.token_run_log_path)
    #
    # def log_data_error

    def log_batch_run_time(self, start_time, end_time):
        # log run_time
        # token_name = self.token_name
        # token_run_log_path = self.token_run_log_path
        run_time = format(end_time - start_time, ".2f")
        # run_time = format(run_time, ".2f")
        token_run_log = read_from_json(self.token_run_log_path)
        token_run_log['run_time'].append(run_time)

        write_to_json(token_run_log, self.token_run_log_path)

        print_and_log(f"token_name={self.token_name}  run_time: {run_time} seconds")

        return token_run_log["is_done"]

