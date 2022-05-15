import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import read_data

net = nn.Sequential(
    nn.Linear(1, 16),
    nn.RReLU(),
    nn.Linear(16, 32),
    nn.RReLU(),
    nn.Linear(32, 64),
    nn.RReLU(),
    nn.Linear(64, 128),
    nn.RReLU(),
    nn.Linear(128, 256),
    nn.RReLU(),
    nn.Linear(256, 256),
    nn.RReLU(),
    nn.Linear(256, 128),
    nn.RReLU(),
    nn.Linear(128, 64),
    nn.RReLU(),
    nn.Linear(64, 32),
    nn.RReLU(),
    nn.Linear(32, 16),
    nn.RReLU(),
    nn.Linear(16, 1)
)
net = net.double()
net.load_state_dict(torch.load("best_net_params.pth"))

x = np.arange(start=1, stop=9, step=0.1)
x = torch.from_numpy(x)

x = torch.unsqueeze(x, dim=1)
y = net(x).T
x = np.arange(start=1, stop=9, step=0.1)
y = y.detach().numpy()
plt.plot(x, y[0], 'r')

d_r_nd = read_data.d_r_nd

read_data.draw_curve_img(d_r_nd)


res = read_data.cal_a_n(d_r_nd[:, :])
read_data.draw_cal_a_n_img(res[0], res[1])

plt.show()
