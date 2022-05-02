import read_data
import numpy as np
import top_n

# TODO: 拿数据写到函数里去，暂时记在这儿
rssi_df = read_data.rssi_df


def cal_one_object_top_n(rssi_lst):
    """
    计算单个物体的topn
    :param rssi_lst: 正值
    :return: 返回topn_idx,topn
    """
    # lst转np.nd
    rssi_nd = np.array(rssi_lst)
    # 取所有rssi大小顺序的下标
    rssi_nd_all_argsort = np.argsort(rssi_nd)[::-1]
    # 截取前TOPN个
    rssi_nd_topn_idx = rssi_nd_all_argsort[0:top_n.Top_N]
    rssi_nd_topn = rssi_nd[rssi_nd_topn_idx]
    # [3 2 1 0]
    # [83.1766 80.9921 77.9977 73.2114]
    return rssi_nd_topn_idx, rssi_nd_topn


def gen_circles_parse(rssi_lst, up_rate=1.0):
    """
    生成单个物体的圆数据
    :param rssi_lst: 正值
    :param up_rate: 增幅
    :return:
    """
    topn_idx, topn_rssi = cal_one_object_top_n(rssi_lst)
    circles_parse = []
    for i in range(len(topn_idx)):
        circles_parse.append([b_ls[topn_idx[i]], cal_d(-topn_rssi[i]) * up_rate])
    return circles_parse

