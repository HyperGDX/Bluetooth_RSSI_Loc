import centroid
import gen_rssi

b_ls = gen_rssi.b_ls
o_l = gen_rssi.o_ls[0]

cal_rssi = gen_rssi.cal_rssi


init_inter = centroid.cal_inter()
init_centroid = centroid.cal_centroid(init_inter)
print("init_centroid: ", init_centroid)
print("raw_pos:       ", o_l)
init_2pos_dist = gen_rssi.cal_2pos_dist(o_l, init_centroid)
print("init_2pos_dist: ", init_2pos_dist)

def amend_one()


