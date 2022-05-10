from graph import Graph
from aco import ACO
import get_distance


graph = Graph()

graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 1)
graph.add_edge("A", "C", 2)
graph.add_edge("H", "G", 2)
graph.add_edge("C", "F", 1)
graph.add_edge("F", "G", 1)
graph.add_edge("G", "F", 1)
graph.add_edge("F", "C", 1)
graph.add_edge("C", "D", 10)
graph.add_edge("E", "D", 2)
graph.add_edge("G", "E", 2)

source = "A"
destination = "D"

aco = ACO(graph)

aco_path, aco_cost = aco.find_shortest_path(source, destination)

print(f"ACO - path: {aco_path}, cost: {aco_cost}")


# Test for finding distance function
grid = [['s', '*', '0', '0'],
        ['0', '*', '*', '*'],
        ['0', '*', '0', '*'],
        ['d', '*', '*', '*']]

print(get_distance.minDistance(grid))
