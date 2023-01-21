from utils.helpers import get_token_run_log_path, print_and_log
from data_processing.helpers import write_to_json, read_from_json


class DataLogger:
    def __init__(self, token_name, to_date):
        self.token_name = token_name
        self.to_date = to_date
        self.token_run_log_path = get_token_run_log_path(token_name)

    def log_no_data(self):
        token_run_log = read_from_json(self.token_run_log_path)
        token_run_log['is_no_data'] = True
        token_run_log["is_error"] = True
        token_run_log["is_done"] = True
        write_to_json(token_run_log, self.token_run_log_path)
        print_and_log(f"token_name={self.token_name}  to_date={self.to_date} -- 'No data is available now'")

    def log_wrong_url(self):
        token_run_log = read_from_json(self.token_run_log_path)
        token_run_log['is_wrong_url'] = True
        token_run_log["is_error"] = True
        token_run_log["is_done"] = True
        write_to_json(token_run_log, self.token_run_log_path)
        # TODO log to a wrong_url list

    def log_run_time_check_is_done(self, start_time, end_time):
        # log run_time and get check is_done
        run_time = format(end_time - start_time, ".2f")
        # run_time = format(run_time, ".2f")
        token_run_log = read_from_json(self.token_run_log_path)
        token_run_log['run_time'].append(run_time)

        write_to_json(token_run_log, self.token_run_log_path)

        print_and_log(f"------done batch token_name={self.token_name} to_date={self.to_date} run_time: {run_time} seconds")

        return token_run_log["is_done"]
