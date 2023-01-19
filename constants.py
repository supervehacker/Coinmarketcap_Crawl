from datetime import datetime


def current_time_yyyymmddhh():
    return datetime.now().strftime("%Y%m%d-%H")


run_date_hour = current_time_yyyymmddhh()
print(f"run_date_hour: {run_date_hour}")
#


TO_DATE = 20221231

TOKEN_TO_CRAWL_PATH = f"data/02_tokens_to_crawl/{run_date_hour}/"
PROCESSING_LOG_PATH = f"data/03_processing/processing_logs/"
PROCESSING_DATA_PATH = f"data/03_processing/processing_data/"

paths = {PROCESSING_DATA_PATH
         # , TEMP_PATH, DATA_LOGS_PATH
, TOKEN_TO_CRAWL_PATH, PROCESSING_LOG_PATH}

L_TOKENS_PATH = f"{TOKEN_TO_CRAWL_PATH}/l_tokens.txt"
L_DONE_TOKENS_PATH = f"{TOKEN_TO_CRAWL_PATH}/l_done_tokens.txt"
L_ERROR_TOKENS_PATH = f"{TOKEN_TO_CRAWL_PATH}/l_error_tokens.txt"


import os
for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # if not os.path.exists(path):
    #     os.makedirs(path)

# import os
# filename = "/foo/bar/baz.txt"
# os.makedirs(os.path.dirname(filename), exist_ok=True)
# print(os.path.dirname(filename))
