import pandas as pd

# 1 3 6 9
# 11 12 13 14
idx_d_map = {
    11: 1,
    12: 3,
    13: 6,
    14: 9
}
raw_df = pd.read_csv("../5.11celiang/data/newdata.CSV")
t = []
d = []
r = []
for i in range(len(raw_df)):
    cur_t, cur_idx, _, cur_r = raw_df.iloc[i]
    if cur_idx in idx_d_map:
        t.append(cur_t)
        d.append(idx_d_map[cur_idx])
        r.append(cur_r)
res = [t, d, r]
print(res)

