import constants as c
from data_master import refresh_l_tokens


def manage_a_worker(token):
    from data_worker import DataWorker
    data_worker = DataWorker(token)
    data_worker.crawl_single_token()


l_tokens = refresh_l_tokens()

# token_name = 'terra-classic'  # url does not exist
token_name = 'golem'    # url has been change
if token_name in l_tokens:
    manage_a_worker(token_name)
else:
    print(f"token_name ={token_name} is not included in l_tokens")

# Write RUN_DATE_HOUR to the file
with open(c.LAST_RUN_DATE_HOUR_PATH, "w") as f:
    f.write(f"{c.RUN_DATE_HOUR}")
