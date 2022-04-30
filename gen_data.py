import torch
from torch.utils.data import Dataset, DataLoader
import os
import pandas as pd
import numpy as np

root_pth = os.getcwd()
data_csv_pth = os.path.join(root_pth, "data", "rssi_3.csv")
name_lst = ["x", "y", "base", "r1", "r2", "r3", "r4"]


class mydataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
        self.data_df = pd.read_csv(data_csv_pth, names=name_lst,header=0)      # 1781*9
        self.loc_df = self.data_df[["x", "y"]]     # 1781*2
        self.rssi_df = self.data_df.drop(
            ["x", "y", "base"], axis=1)     # 1781*6

    def __getitem__(self, index):
        x = self.rssi_df.iloc[index].to_numpy().astype(np.float32)
        y = self.loc_df.iloc[index].to_numpy().astype(np.float32)
        return torch.tensor(x), torch.tensor(y)

    def __len__(self):
        return self.data_df.shape[0]
