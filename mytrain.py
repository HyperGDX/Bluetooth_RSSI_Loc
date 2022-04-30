import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader, random_split
import gen_data

net = nn.Sequential(
    nn.Linear(4,16),
    nn.ReLU(),
    nn.Linear(16,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16,8),
    nn.ReLU(),
    nn.Linear(8,2)
    )

dataset = gen_data.mydataset()
train_dataset = dataset
train_dataloader = DataLoader(train_dataset, batch_size=64, shuffle=True)

epochs = 2000

loss_fun = nn.MSELoss()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = net.to(device)
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
best_loss = 1000.0
for epoch in range(epochs):
    net.train()
    sum_loss = 0.0
    for idx,(img, label) in enumerate(train_dataloader):        
        img, label = img.to(device), label.to(device)
        optimizer.zero_grad()
        output = net(img)
        train_loss = loss_fun(output, label)
        train_loss.backward()
        optimizer.step()
        sum_loss += train_loss.item()
    final_loss = sum_loss/idx
    if final_loss < best_loss:
        best_loss = final_loss
        torch.save(net.state_dict(),'best_net_params.pth')
    print('[%d] Train loss:%.09f' % (epoch, final_loss))

    # if epoch % 100==0:
    #     net.eval()
    #     eval_loss = 0.
    #     for img, label in test_dataloader:
    #         img, label = img.to(device), label.to(device)
    #         out = net(img)
    #         loss = loss_fun(out, label)
    #         eval_loss += loss.item()

    #     print('Test[%d] loss:%.03f' % (epoch+1,(eval_loss / (len(test_dataset)))))


