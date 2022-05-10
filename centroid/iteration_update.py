import centroid
import gen_rssi
import parse
import read_data
import cal_func
import top_n

Top_N = parse.Top_N
b_ls = read_data.beacon_loc_lst_tuple
o_l = (3, 4)

raw_rssi = read_data.rssi_df.iloc[0]
init_topn_idx, init_topn = top_n.cal_one_object_top_n(raw_rssi)

init_topn_pos = cal_func.get_topn_beacon_pos(read_data.beacon_loc_lst_tuple, init_topn_idx)
print(init_topn_pos)

init_inter = centroid.cal_inter(init_topn, init_topn_pos)
init_centroid = centroid.cal_centroid(init_inter)
print("init_centroid: ", init_centroid)
print("raw_pos:       ", o_l)
init_2pos_dist = cal_func.cal_2pos_dist(o_l, init_centroid)
print("init_2pos_dist: ", init_2pos_dist)

topn_idx, topn_rssi = top_n.cal_one_object_top_n(raw_rssi)
print(topn_idx, topn_rssi)

topn_idx_r = topn_idx[::-1]
topn_rssi_r = topn_rssi[::-1]
amended_topn_rssi_r = []


def amend_beacons():
    for i in range(Top_N):
        cur_beacon_loc = b_ls[topn_idx_r[i]]
        amended_topn_rssi_r.append(round(cal_func.d2rssi(cal_func.cal_2pos_dist(cur_beacon_loc, init_centroid)), 4))


print("***********")
amend_beacons()
# print("init_topn_rssi:      ", topn_rssi)
# print("amended_topn_rssi_r: ", amended_topn_rssi_r[::-1])
# init_topn_rssi:       [83.1766 80.9921 77.9977 73.2114]
# amended_topn_rssi_r:  [83.0418, 80.8781, 78.0314, 73.4293]

amended_rssis = amended_topn_rssi_r[::-1]
amended_inter = centroid.cal_inter(amended_rssis, init_topn_pos)
amended_centroid = centroid.cal_centroid(amended_inter)
amended_2pos_dist = cal_func.cal_2pos_dist(o_l, amended_centroid)

print("init_topn_rssi:      ", topn_rssi)
print("amended_topn_rssi_r: ", amended_topn_rssi_r[::-1])
print("raw_pos:       ", o_l)
print("init_centroid: ", init_centroid)
print("amended_centroid: ", amended_centroid)
print("init_2pos_dist: ", init_2pos_dist)
print("amended_2pos_dist: ", amended_2pos_dist)
