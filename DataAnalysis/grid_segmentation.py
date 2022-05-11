from matplotlib import pyplot as plt
import numpy as np

resolution = 30
y = np.arange(0,resolution,1)
x = np.arange(0,resolution,1)

Y,X = np.meshgrid(y,x) 

maxf = np.zeros(shape = Y.shape)
maxf.fill(-9999.99) 
index = []
delta = int(resolution/3)
end = int(resolution*2 + delta)
for k in range(0, end, delta):
    for i,x_ in enumerate(x):
        for j, y_ in enumerate(y):
            if y_ < ((k+delta)-x_) and y_ >= (k-x_):
                maxf[i,j]=6-int(k/delta)
    index.append(int(k/delta))

plt.contourf(X,Y,maxf,index)
plt.colorbar()
plt.show()
