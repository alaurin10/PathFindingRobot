from typing import final
import Coords2Image
import matplotlib.pyplot as plt
import numpy as np
import random
from CreateNodes import create_nodes
from graph import Graph
from aco import ACO


resolution = 30
probability = 4 # Probability in percent
image = Coords2Image.Convert2Image('OBJ01_pts.txt', resolution)

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
                    image[i][j] = 2
                    points[f'{point_index}'] = k/delta,i,j
                    point_index += 1
    region = k/delta

points['0'] = (0.0, 1, 1)
image[1][1] = 2
points[str(point_index)] = (region-1, resolution-2, resolution-2)
print(points)

edges = create_nodes(points, 5, image)

graph = Graph()

source = '0'
destination = str(len(points)-1)
for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])

aco = ACO(graph)
aco_path, aco_cost = aco.find_shortest_path(source, destination)
print(f"ACO - path: {aco_path}, cost: {aco_cost}")

plt.figure()
x_aco = []
y_aco = []
for node in aco_path:
    x_aco.append(points[node][1])
    y_aco.append(points[node][2])
plt.plot(x_aco,y_aco, zorder=2)

plt.imshow(image, cmap='Greys')

plt.show()
