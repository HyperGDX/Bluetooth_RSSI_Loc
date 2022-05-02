import math


def cal_2pos_dist(pos1, pos2):
    """
    计算两点之间的距离
    :param pos1: tuple(x1,y1)
    :param pos2: tuple(x2,y2)
    :return: float(d)
    """
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def cal_rssi(b_l, o_l, a=-47, n=3.75):
    t = cal_2pos_dist(b_l, o_l)
    return round(a - 10 * n * math.log10(t), 4)


def cal_d(rssi, a=-45, n=4):
    a = a
    n = n
    d = 10 ** ((a - rssi) / (10 * n))
    return d
