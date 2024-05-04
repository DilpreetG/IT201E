'''Lab 5 - IT201E - Michael Jolley and Dilpreet Gill - 4/30/2024'''

import heapq
import networkx
import matplotlib
from matplotlib import pyplot as plt


def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            if weight < 0:
                return("Negative weights are not supported")
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def visualize_graph(graph, shortest_paths, start_vertex):
    G = networkx.DiGraph()

    for node, edges in graph.items():
        for edge in edges:
            if edge[1] < 0:
                return("Negative weights are not supported")
            G.add_edge(node, edge[0], weight=edge[1])

    pos = networkx.spring_layout(G)
    networkx.draw(G, pos, with_labels=True)
    labels = networkx.get_edge_attributes(G, 'weight')
    networkx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Create the shortest path tree
    shortest_path_tree_edges = [(start_vertex, node) for node in shortest_paths.keys() if node != start_vertex]
    networkx.draw_networkx_edges(G, pos, edgelist=shortest_path_tree_edges, edge_color='r', width=2)

    plt.show()

# Test cases
test_cases = {
    "Test Case #1: Simple Graph": {
        "graph": {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', 2), ('D', 6)],
            'C': [('D', 3)],
            'D': []
        },
        "start_vertex": 'A',
        "expected_output": {'A': 0, 'B': 1, 'C': 3, 'D': 6}
    },
    "Test Case #2: Graph with Negative Weights": {
        "graph": {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', -2), ('D', 6)],
            'C': [('D', 3)],
            'D': []
        },
        "start_vertex": 'A',
        "expected_output": "Error: Negative weights are not supported"
    },
    "Test Case #3: Dense Graph": {
        "graph":
            {
            'A': [('B', 1), ('C', 4), ('D', 2), ('E', 5), ('F', 3)],
            'B': [('A', 1), ('C', 2), ('D', 3), ('E', 4), ('F', 2)],
            'C': [('A', 4), ('B', 2), ('D', 1), ('E', 3), ('G', 1)],
            'D': [('A', 2), ('B', 3), ('C', 1), ('E', 2), ('G', 4)],                'E': [('A', 5), ('B', 4), ('C', 3), ('D', 2), ('H', 2)],
            'F': [('A', 3), ('B', 2), ('C', 1), ('H', 3)],
            'G': [('D', 4), ('E', 3), ('H', 1)],
            'H': [('F', 2), ('G', 1), ('E', 2), ('I', 2)],
            'I': [('H', 2), ('J', 2)],
            'J': [('I', 2), ('A', 2), ('B', 3), ('C', 4), ('D', 5), ('E', 6)],
            },
        "start_vertex": 'A',
        "expected_output": {
            'A': 0, 'B': 1, 'C': 3, 'D': 6, 'E': 5
        }
    },
}

for name, params in test_cases.items():
    print(f"{name}:")
    shortest_paths = dijkstra(params["graph"], params["start_vertex"])
    print(shortest_paths)
    visualize_graph(params["graph"], shortest_paths, params["start_vertex"])
