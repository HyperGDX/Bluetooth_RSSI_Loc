import numpy as np
import math

# m个基站
b_ls = [(0, 0), (0, 10), (10, 0), (10, 10), (5, 5)]
# n个待测
o_ls = [(3, 4), (6, 6)]


def cal_2pos_dist(b_l, o_l):
    return math.sqrt((b_l[0] - o_l[0]) ** 2 + (b_l[1] - o_l[1]) ** 2)


def cal_rssi(b_l, o_l, A=-47, n=3.75):
    t = cal_2pos_dist(b_l, o_l)
    return A - 10 * n * math.log10(t)


def cal_rssis(b_ls, o_ls):
    rssi_lst = []
    for o_l in o_ls:
        rssi_o_lst = []
        for b_l in b_ls:
            rssi_o_lst.append(round(cal_rssi(o_l, b_l), 4))
        rssi_lst.append(rssi_o_lst)
    return rssi_lst
