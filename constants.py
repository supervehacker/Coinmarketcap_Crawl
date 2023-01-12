TO_DATE = 20221231
DATA_LOGS_PATH = "data_logs/"
DATA_PATH = "output/"
TEMP_PATH = "temp/"

paths = [DATA_LOGS_PATH, DATA_PATH, TEMP_PATH]
import os
for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)




from datetime import datetime

def current_time_yyyymmddhh():
    return datetime.now().strftime("%Y%m%d%H")

print(current_time_yyyymmddhh())

XXX = f"{current_time_yyyymmddhh()}_{DATA_PATH}"