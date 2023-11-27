import networkx as nx
import numpy as np


def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def create_complete_graph(points):
    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            G.add_edge(i, j, weight=distance)
    return G


def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)


def odd_vertices(subgraph):
    odd = []
    for node in subgraph.nodes():
        if subgraph.degree(node) % 2 != 0:
            odd.append(node)
    return odd


def minimum_weight_perfect_matching(graph, odd_vertices):
    odd_graph = graph.subgraph(odd_vertices)
    return nx.algorithms.matching.max_weight_matching(odd_graph, maxcardinality=True)


def eulerian_circuit(graph):
    return list(nx.eulerian_circuit(graph))


def christofides_tsp(points):
    complete_graph = create_complete_graph(points)
    min_spanning_tree = minimum_spanning_tree(complete_graph)
    odd_vert = odd_vertices(min_spanning_tree)
    min_weight_matching = minimum_weight_perfect_matching(complete_graph, odd_vert)

    augmented_graph = complete_graph.copy()
    for edge in min_weight_matching:
        augmented_graph.add_edge(edge[0], edge[1], weight=complete_graph[edge[0]][edge[1]]['weight'])

    eulerian_circuit_edges = eulerian_circuit(augmented_graph)

    visited = set()
    circuit = []
    for edge in eulerian_circuit_edges:
        if edge[0] not in visited:
            circuit.append(edge[0])
            visited.add(edge[0])

    circuit.append(circuit[0])

    circuit = list(dict.fromkeys(circuit))

    total = sum(complete_graph[circuit[i]][circuit[i + 1]]['weight'] for i in range(len(circuit) - 1))

    return circuit, total


points = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
optimal_path, total_cost = christofides_tsp(points)
print("Optimal Path:", optimal_path)
print("Total Cost:", total_cost)
