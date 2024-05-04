'''Lab 5 - IT201E - Michael Jolley and Dilpreet Gill - 4/30/2024'''

import heapq
import networkx
import matplotlib


def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def visualize_graph(graph, shortest_paths, start_vertex):
    G = networkx.DiGraph()

    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge[0], weight=edge[1])

    pos = networkx.spring_layout(G)
    networkx.draw(G, pos, with_labels=True)
    labels = networkx.get_edge_attributes(G, 'weight')
    networkx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    shortest_path_edges = [(start_vertex, node) for node in shortest_paths.keys()]
    networkx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=2)

    matplotlib.show()

# Test cases
test_cases = {
    "Test Case #1": {
        "graph": {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', 2), ('D', 6)],
            'C': [('D', 3)],
            'D': []
        },
        "start_vertex": 'A'
    },
    # Add more test cases here
}

for name, params in test_cases.items():
    print(f"{name}:")
    shortest_paths = dijkstra(params["graph"], params["start_vertex"])
    print(shortest_paths)
    visualize_graph(params["graph"], shortest_paths, params["start_vertex"])

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(dijkstra(graph, 'A'))
