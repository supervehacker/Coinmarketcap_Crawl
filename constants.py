from datetime import datetime


def current_time_yyyymmddhh():
    return datetime.now().strftime("%Y%m%d-%H")


RUN_DATE_HOUR = current_time_yyyymmddhh()
print(f"run_date_hour: {RUN_DATE_HOUR}")





TO_DATE = 20221231

LIST_ALL_TOKENS_PATH = f"data/01_list_all_tokens/"
TOKEN_TO_CRAWL_PATH = f"data/02_tokens_to_crawl/{RUN_DATE_HOUR}/"
PROCESSING_LOG_PATH = f"data/03_processing/processing_logs/"
PROCESSING_DATA_PATH = f"data/03_processing/processing_data/"

paths = {PROCESSING_DATA_PATH, TOKEN_TO_CRAWL_PATH, PROCESSING_LOG_PATH}

import os
for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # if not os.path.exists(path):
    #     os.makedirs(path)


def get_l_tokens_paths(token_to_crawl_path):
    l_tokens_path = f"{token_to_crawl_path}/l_tokens.txt"
    l_done_tokens_path = f"{token_to_crawl_path}/l_done_tokens.txt"
    l_error_tokens_path = f"{token_to_crawl_path}/l_error_tokens.txt"
    return l_tokens_path, l_done_tokens_path, l_error_tokens_path


# L_TOKENS_PATH = f"{TOKEN_TO_CRAWL_PATH}/l_tokens.txt"
# L_DONE_TOKENS_PATH = f"{TOKEN_TO_CRAWL_PATH}/l_done_tokens.txt"
# L_ERROR_TOKENS_PATH = f"{TOKEN_TO_CRAWL_PATH}/l_error_tokens.txt"
L_TOKENS_PATH, L_DONE_TOKENS_PATH, L_ERROR_TOKENS_PATH = get_l_tokens_paths(TOKEN_TO_CRAWL_PATH)


RUN_DATE_HOUR_PATH = f"{PROCESSING_LOG_PATH}/last_run_date_hour.txt"
try:
    with open(RUN_DATE_HOUR_PATH, "r") as f:  # get last_run_date_hour from run_date_hour.txt
        last_run_date_hour = f.readlines()[0]
except FileNotFoundError:
    last_run_date_hour = RUN_DATE_HOUR

LAST_RUN_DATE_HOUR = last_run_date_hour
LAST_TOKEN_TO_CRAWL_PATH = f"data/02_tokens_to_crawl/{LAST_RUN_DATE_HOUR}/"

ALL_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}/all_tokens.txt"
ALL_DONE_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}/all_done_tokens.txt"
ALL_ERROR_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}/all_error_tokens.txt"
ALL_UNDONE_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}/all_undone_tokens.txt"


# import os
# filename = "/foo/bar/baz.txt"
# os.makedirs(os.path.dirname(filename), exist_ok=True)
# print(os.path.dirname(filename))
