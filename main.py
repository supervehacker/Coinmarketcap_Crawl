# from utils.helpers import *
from data_master import *

# sys.stdout = Logger("mylog.log")  # redirect print function to log file


# data_master = DataMaster()
# l_tokens = data_master.refresh_l_tokens()
# for token_name in l_tokens:
#     data_worker = DataWorker(token_name)
#     data_worker.crawl_single_token()
#     break
#
print("Start the program")

data_master = DataMaster()
l_tokens = data_master.refresh_l_tokens()
data_master.manage_workers(num_workers=3, l_tokens=l_tokens)
