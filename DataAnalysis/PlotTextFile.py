import matplotlib.pyplot as plt
import Coords2Image
import numpy as np
import random
from CreateNodes import create_nodes

# Read in contents of each txt file. Split coordnites into a nested list
object1 = [x.split() for x in open('OBJ01_pts.txt').read().split('\n') if x != '']
object1 = [list(map(float, lst)) for lst in object1]

object2 = [x.split() for x in open('OBJ02_pts.txt').read().split('\n') if x != '']
object2 = [list(map(float, lst)) for lst in object2]

# Create x and y coords from index 0 and 2 of the lists. Index 1 is unused
x = []
y = []
for i in range(84,len(object1)):
    x.append(object1[i][0])
    y.append(object1[i][2])

# # Plot the x,y coords of room 1 in a new figure
# plt.figure()
# plt.plot(x,y)
# plt.plot([1, -1, -1, 1, 1], [1, 1, -1, -1, 1]) # Add box to center of figure
# plt.title('Room 1')


# Create x and y coords from index 0 and 2 of the lists. Index 1 is unused
x = []
y = []
for i in range(len(object2)):
    x.append(object2[i][0])
    y.append(object2[i][2])


# # Plot the x,y coords of room 1 in a new figure
# plt.figure()
# plt.plot(x,y)
# plt.title('Room 2')
# plt.show()  # Show both figures

# Display binary image converted from the coordinates
resolution = 30
probability = 7 # Probability in percent
image = Coords2Image.Convert2Image('OBJ01_pts.txt', resolution)
# plt.figure()
# plt.imshow(image, cmap='Greys')
# plt.show()

image = image.tolist()
points = {}
point_index = 0

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
                if random.random() < probability/100:
                    if image[i][j] == 1:
                        continue
                    image[i][j] = 3
                    points[f'{point_index}'] = k/delta,i,j
                    point_index += 1
    index.append(int(k/delta))

nodes = create_nodes(points, point_index)

plt.imshow(image, cmap='Greys')

plt.contourf(X,Y,maxf,index)
plt.colorbar()

plt.show()
print(points)
