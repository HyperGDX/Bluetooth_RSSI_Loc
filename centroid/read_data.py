import pandas as pd
import os

root_pth = os.pardir
data_csv_pth = os.path.join(root_pth, "data", "test_rssi.csv")
rssi_df = pd.read_csv(data_csv_pth)
beacon_loc_lst_tuple = list()
for b in rssi_df.columns:
    aa = b.split(',')
    beacon_loc_lst_tuple.append((int(aa[0][1:]), int(aa[1][:-1])))