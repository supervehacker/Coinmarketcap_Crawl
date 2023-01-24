from utils.date_helpers import current_time_yyyymmddhh

RUN_DATE_HOUR = current_time_yyyymmddhh()

TO_DATE = 20221231

LIST_ALL_TOKENS_PATH = f"data/01_list_all_tokens/"
TOKEN_TO_CRAWL_PATH = f"data/02_tokens_to_crawl/{RUN_DATE_HOUR}/"
PROCESSING_PATH = f"data/03_processing/"
PROCESSING_DATA_PATH = f"{PROCESSING_PATH}processing_data/"
PROCESSING_RUN_LOG_PATH = f"{PROCESSING_PATH}processing_run_logs/"
PROCESSING_ERROR_LOG_PATH = f"{PROCESSING_PATH}processing_error_logs/"
OUTPUT_DATA_PATH = f"data/04_output/output_data/"
OUTPUT_LOG_PATH = f"data/04_output/data_run_logs/"

paths = {TOKEN_TO_CRAWL_PATH, PROCESSING_DATA_PATH, PROCESSING_RUN_LOG_PATH, PROCESSING_ERROR_LOG_PATH, OUTPUT_DATA_PATH, OUTPUT_LOG_PATH}


for path in paths:
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # if not os.path.exists(path):
    #     os.makedirs(path)


def get_l_tokens_paths(token_to_crawl_path):
    l_tokens_path = f"{token_to_crawl_path}l_tokens.txt"
    l_done_tokens_path = f"{token_to_crawl_path}l_done_tokens.txt"
    l_error_tokens_path = f"{token_to_crawl_path}l_error_tokens.txt"
    return l_tokens_path, l_done_tokens_path, l_error_tokens_path


L_TOKENS_PATH, L_DONE_TOKENS_PATH, L_ERROR_TOKENS_PATH = get_l_tokens_paths(TOKEN_TO_CRAWL_PATH)
# print(L_TOKENS_PATH, L_DONE_TOKENS_PATH, L_ERROR_TOKENS_PATH)
LOG_FILE_PATH = f"{TOKEN_TO_CRAWL_PATH}mylog.log"

ALL_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}all_tokens.txt"
ALL_DONE_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}all_done_tokens.txt"
ALL_ERROR_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}all_error_tokens.txt"
ALL_UNDONE_TOKENS_PATH = f"{LIST_ALL_TOKENS_PATH}all_undone_tokens.txt"


LAST_RUN_DATE_HOUR_PATH = f"{PROCESSING_PATH}last_run_date_hour.txt"
try:
    with open(LAST_RUN_DATE_HOUR_PATH, "r") as f:  # get last_run_date_hour from run_date_hour.txt
        last_run_date_hour = f.readlines()[0]

except FileNotFoundError:
    last_run_date_hour = None
    from data_processing.helpers import write_list_to_txt, read_list_from_txt
    write_list_to_txt(read_list_from_txt(ALL_TOKENS_PATH), ALL_UNDONE_TOKENS_PATH)

LAST_RUN_DATE_HOUR = last_run_date_hour
LAST_TOKEN_TO_CRAWL_PATH = f"data/02_tokens_to_crawl/{LAST_RUN_DATE_HOUR}/"
print(f"run_date_hour: {RUN_DATE_HOUR}; last_run_date_hour: {last_run_date_hour}")

# import os
# filename = "/foo/bar/baz.txt"
# os.makedirs(os.path.dirname(filename), exist_ok=True)
# print(os.path.dirname(filename))
