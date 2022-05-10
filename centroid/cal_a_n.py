import numpy as np
from scipy import optimize

import cal_func
import read_data
import test_data


def d2r_func(x, a, b):
    return a + b * np.log10(x)


o_ls = test_data.o_ls
beacon_loc_lst_tuple = read_data.beacon_loc_lst_tuple
raw_rssi = read_data.rssi_df


# TODO:改个topn版的
def gen_x_y(rssi_df, o_ls, top_n=4):
    x = []
    y = []
    idx_min = rssi_df.idxmin(axis=1)
    rssi_min = rssi_df.min(axis=1)
    for i in range(len(rssi_df)):
        y.append(rssi_min[i])
        aa = idx_min[i].split(',')
        x.append(cal_func.cal_2pos_dist((int(aa[0][1:]), int(aa[1][:-1])), o_ls[i]))
    return x, y


def cal_a_n(rssi_df, o_ls):
    x0, y0 = gen_x_y(rssi_df, o_ls)
    a4, b4 = optimize.curve_fit(d2r_func, x0, y0)[0]
    return round(a4, 4), round(b4, 4)


print(cal_a_n(raw_rssi, o_ls))
