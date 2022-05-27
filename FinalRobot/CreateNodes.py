import get_distance
import copy


def create_nodes(points, num_regions, grid):

    edges = []
    for i in range(num_regions):
        first_region = []
        second_region = []
        
        for key, value in points.items():
            if value[0] == int(i):
                first_region.append([key, value[1], value[2]])
            if value[0] == int(i+1):
                second_region.append([key, value[1], value[2]])

        grid_copy = []
        for node1 in first_region:
            for node2 in second_region:                
                grid_copy = copy.copy(grid)
                grid_copy[node1[1]][node1[2]] = 's'
                grid_copy[node2[1]][node2[2]] = 'd'
                dist = get_distance.minDistance(grid_copy)
                if not dist == -1:
                    edges.append((node1[0], node2[0], dist))
                grid_copy[node1[1]][node1[2]] = 2
                grid_copy[node2[1]][node2[2]] = 2
                
    return edges

