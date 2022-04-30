import matplotlib
from matplotlib import pyplot as plt
import numpy as np 





def draw_loss_img(epoches=1000,loss_max=10):
    plt.style.use('_mpl-gallery')

    losses = []
    with open(r'test2.log','r') as f:
        for idx,line in enumerate(f) :
            if idx<epoches:
                losses.append(np.float64(line.split(':')[1].strip()))
            else:
                break
            
    y = np.array(losses)
    x = np.arange(epoches,dtype=np.int16)
    plt.plot(x, y, linewidth=2.0)

    plt.xlim=((0, epoches))
    plt.xticks=np.arange(0, epoches,100)

    plt.ylim=((0, loss_max))
    plt.yticks=np.arange(0, loss_max,1)

    plt.xlabel('epoch')
    plt.ylabel('loss')

    plt.show()

draw_loss_img()