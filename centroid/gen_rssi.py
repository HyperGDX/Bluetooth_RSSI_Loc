import os
import random

import numpy as np
import pandas as pd

import cal_func
import test_data


def gen_rssi(beacon_pos_lst, object_pos, suiji=False, a=-47, n=3.75):
    rssi_lst = []
    for b_l in beacon_pos_lst:
        if not suiji:
            rssi_lst.append(cal_func.d2rssi(cal_func.cal_2pos_dist(object_pos, b_l), a, n))
        else:
            mu = 0
            sigma = 0.05
            rssi_lst.append(cal_func.d2rssi(cal_func.cal_2pos_dist(object_pos, b_l),
                                            a + random.gauss(mu, sigma),
                                            n + random.gauss(mu, sigma)))
    return rssi_lst


def gen_rssis(beacon_pos_lst, object_pos_lst, suiji=False):
    rssi_lst_lst = []
    for o_l in object_pos_lst:
        if suiji:
            rssi_lst_lst.append(gen_rssi(beacon_pos_lst, o_l, suiji=True))
        else:
            rssi_lst_lst.append(gen_rssi(beacon_pos_lst, o_l))
    return rssi_lst_lst


rssi_data = gen_rssis(test_data.b_ls, test_data.o_ls, suiji=True)
rssi_df = pd.DataFrame(np.array(rssi_data))
rssi_df.columns = [test_data.b_ls]
print(rssi_df)
root_pth = os.pardir
data_csv_pth = os.path.join(root_pth, "data", "test_rssi.csv")
rssi_df.to_csv(path_or_buf=data_csv_pth, index=False)
