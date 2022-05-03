import math
import numpy as np
import read_data


def cal_2pos_dist(pos1, pos2):
    """
    计算两点之间的距离
    :param pos1: tuple(x1,y1)
    :param pos2: tuple(x2,y2)
    :return: float(d)
    """
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def d2rssi(d, a=-47, n=3.75):
    return -1 * round(a - 10 * n * math.log10(d), 4)


def rssi2d(rssi, a=-45, n=4):
    a = a
    n = n
    d = 10 ** ((a + rssi) / (10 * n))
    return d


def rssi_check_positive(rssi):
    if rssi[0] > 0:
        return rssi
    else:
        return -1.0 * rssi


def get_topn_beacon_pos(all_beacon_pos, select_beacon_idx):
    beacon_pos_lst = []
    for i in select_beacon_idx:
        beacon_pos_lst.append(all_beacon_pos[i])
    return beacon_pos_lst
