import constants as c

from datetime import datetime

import sys

from utils.date_helpers import subtract_days_from_date


# import datetime
# redirect print function to log file
class Logger(object):
    def __init__(self, file_name="Default.log"):
        self.terminal = sys.stdout
        self.log = open(file_name, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(f"{datetime.now()}: {message}")

    def flush(self):  # avoid this msg: AttributeError: 'Logger' object has no attribute 'flush'
        pass
# sys.stdout = Logger("mylog.log") # redirect print function to log file


# Create a dict to get batch_no
to_date1 = c.TO_DATE
date_batch_map = {}
for i in range(40):  # to around 20120319 / first token: 20130428
    to_date2 = subtract_days_from_date(to_date1, 100)
    date_batch_map[to_date1] = i + 1
    to_date1 = subtract_days_from_date(to_date2, 1)

# print(date_batch_map)
# {20221231: 1, 20220921: 2, 20220612: 3, 20220303: 4, 20211122: 5, 20210813: 6, 20210504: 7, 20210123: 8, 20201014: 9, 20200705: 10, 20200326: 11, 20191216: 12, 20190906: 13, 20190528: 14, 20190216: 15, 20181107: 16, 20180729: 17, 20180419: 18, 20180108: 19, 20170929: 20, 20170620: 21, 20170311: 22, 20161130: 23, 20160821: 24, 20160512: 25, 20160201: 26, 20151023: 27, 20150714: 28, 20150404: 29, 20141224: 30, 20140914: 31, 20140605: 32, 20140224: 33, 20131115: 34, 20130806: 35, 20130427: 36, 20130116: 37, 20121007: 38, 20120628: 39, 20120319: 40}


def get_token_run_log_path(token_name):
    return f"{c.TEMP_PATH}{token_name}_run_log.json"
