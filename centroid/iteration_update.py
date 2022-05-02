import centroid
import gen_rssi
import top_n

Top_N = top_n.Top_N
b_ls = gen_rssi.b_ls
o_l = gen_rssi.o_ls[0]

cal_rssi = gen_rssi.cal_rssi
test_rssi_lsts = top_n.test_rssi_lsts
init_inter = centroid.cal_inter(test_rssi_lsts[0])
init_centroid = centroid.cal_centroid(init_inter)
print("init_centroid: ", init_centroid)
print("raw_pos:       ", o_l)
init_2pos_dist = gen_rssi.cal_2pos_dist(o_l, init_centroid)
print("init_2pos_dist: ", init_2pos_dist)

topn_idx, topn_rssi = top_n.cal_one_object_top_n(top_n.test_rssi_lsts[0])
# print(topn_idx, topn_rssi)

topn_idx_r = topn_idx[::-1]
topn_rssi_r = topn_rssi[::-1]

amended_topn_rssi_r = []


def amend_beacons():
    for i in range(Top_N):
        cur_beacon_loc = b_ls[topn_idx_r[i]]
        amended_topn_rssi_r.append(round(cal_rssi(cur_beacon_loc, init_centroid), 4))


amend_beacons()
print("init_topn_rssi:      ", topn_rssi)
print("amended_topn_rssi_r: ", amended_topn_rssi_r[::-1])
# init_topn_rssi:       [83.1766 80.9921 77.9977 73.2114]
# amended_topn_rssi_r:  [83.0418, 80.8781, 78.0314, 73.4293]

amended_rssis = amended_topn_rssi_r[::-1]
amended_inter = centroid.cal_inter(amended_rssis)
amended_centroid = centroid.cal_centroid(amended_inter)
print("amended_centroid: ", amended_centroid)