from data_master import *
import argparse


# create parser
parser = argparse.ArgumentParser()
parser.add_argument("num_workers", type=int, help="number of concurrent workers")
args = parser.parse_args()
# sys.stdout = Logger("mylog.log")  # redirect print function to log file


# data_master = DataMaster()
# l_tokens = data_master.refresh_l_tokens()
# for token_name in l_tokens:
#     data_worker = DataWorker(token_name)
#     data_worker.crawl_single_token()
#     break aa

num_workers = args.num_workers
# num_workers = 1

print(f"Start the program with {num_workers} workers")

data_master = DataMaster()
l_tokens = data_master.refresh_l_tokens()
data_master.manage_workers(num_workers=num_workers, l_tokens=l_tokens)
