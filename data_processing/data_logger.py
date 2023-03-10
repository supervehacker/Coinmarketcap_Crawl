from utils.helpers import get_token_run_log_path, print_and_log
from data_processing.helpers import write_to_json, read_from_json


class DataLogger:
    def __init__(self, token_name, to_date):
        self.token_name = token_name
        self.to_date = to_date
        self.token_run_log_path = get_token_run_log_path(token_name)

    def write_run_log_to_json(self, token_run_log: dict):
        write_to_json(token_run_log, self.token_run_log_path)

    def append_run_time_to_run_log(self, token_run_log: dict, start_time):
        import time
        end_time = time.time()
        run_time = format(end_time - start_time, ".2f")
        token_run_log['run_time'].append(run_time)
        print_and_log(f"----- run_time: {run_time} seconds -- token_name={self.token_name} to_date={self.to_date}")
        return token_run_log

    def log_no_data_error(self):
        token_run_log = read_from_json(self.token_run_log_path)
        token_run_log['is_no_data'] = True
        token_run_log["is_error"] = True
        # token_run_log["is_done"] = True
        # write_to_json(token_run_log, self.token_run_log_path)
        self.write_run_log_to_json(token_run_log)
        print_and_log(f"-- 'No data is available now' -- token_name={self.token_name}  to_date={self.to_date}")

    """
    def log_wrong_url(self):
        token_run_log = read_from_json(self.token_run_log_path)
        token_run_log['is_wrong_url'] = True
        token_run_log["is_error"] = True
        # token_run_log["is_done"] = True
        # write_to_json(token_run_log, self.token_run_log_path)
        self.write_run_log_to_json(token_run_log)
        # TODO append to a wrong_url list
    """

    # def log_run_time_check_is_done(self, start_time, end_time):
    #     # log run_time and get check is_done
    #     run_time = format(end_time - start_time, ".2f")
    #     token_run_log = read_from_json(self.token_run_log_path)
    #     token_run_log['run_time'].append(run_time)
    #
    #     # write_to_json(token_run_log, self.token_run_log_path)
    #     self.write_token_run_log(token_run_log)
    #
    #     print_and_log(f"------done batch token_name={self.token_name} to_date={self.to_date} run_time: {run_time} seconds")
    #
    #     return token_run_log["is_done"]
