import cal_func
import os
import test_data
import pandas as pd
import numpy as np


def gen_rssi(beacon_pos_lst, object_pos):
    rssi_lst = []
    for b_l in beacon_pos_lst:
        rssi_lst.append(cal_func.d2rssi(cal_func.cal_2pos_dist(object_pos, b_l)))
    return rssi_lst


def gen_rssis(beacon_pos_lst, object_pos_lst):
    rssi_lst_lst = []
    for o_l in object_pos_lst:
        rssi_lst_lst.append(gen_rssi(beacon_pos_lst, o_l))
    return rssi_lst_lst


rssi_data = gen_rssis(test_data.b_ls, test_data.o_ls)
rssi_df = pd.DataFrame(np.array(rssi_data))
rssi_df.columns = [test_data.b_ls]
print(rssi_df)
root_pth = os.pardir
data_csv_pth = os.path.join(root_pth, "data", "test_rssi.csv")
rssi_df.to_csv(path_or_buf=data_csv_pth, index=False)
