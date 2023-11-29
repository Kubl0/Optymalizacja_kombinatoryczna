from itertools import permutations

import networkx as nx
import numpy as np


def triangle(e1, e2, e3):
    return e1 + e2 >= e3 and e1 + e3 >= e2 and e2 + e3 >= e1


def traingle_inequality(G):
    for node in G.nodes():
        for neighbor in G.neighbors(node):
            for neighbor2 in G.neighbors(node):
                if neighbor != neighbor2:
                    if not triangle(G[node][neighbor]['weight'], G[node][neighbor2]['weight'],
                                    G[neighbor][neighbor2]['weight']):
                        return False
    return True


def min_perfect_matching(G):
    # maximal_matching = nx.maximal_matching(G)
    # min_weight_matching = None
    # min_weight = np.inf
    #
    # for permuted_matching in permutations(maximal_matching):
    #     weight = sum(G[edge[0]][edge[1]]['weight'] for edge in permuted_matching)
    #
    #     if weight < min_weight:
    #         min_weight = weight
    #         min_weight_matching = permuted_matching

    is_perfect = nx.is_perfect_matching(G, nx.min_weight_matching(G))
    if not is_perfect:
        raise Exception('Cannot find a perfect matching')

    return nx.min_weight_matching(G)


def christofides(G):
    if not traingle_inequality(G):
        return Exception("Graph does not satisfy triangle inequality")

    # 1
    T = nx.minimum_spanning_tree(G)

    # 2
    O = G.subgraph([node for node, degree in T.degree() if degree % 2 == 1])
    M = min_perfect_matching(O)

    # 3
    H = nx.MultiGraph(T)
    H.add_edges_from(M)

    # 4
    eulerian_circuit = nx.eulerian_circuit(H)

    # 5

    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if u not in hamiltonian_circuit:
            hamiltonian_circuit.append(u)
        if v not in hamiltonian_circuit:
            hamiltonian_circuit.append(v)

    # hamiltonian_circuit.append(hamiltonian_circuit[0])

    weight = 0
    for i in range(len(hamiltonian_circuit) - 1):
        weight += G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight']

    return hamiltonian_circuit, weight


if __name__ == "__main__":
    G = nx.Graph()
    # G.add_nodes_from([0, 1, 2, 3, 4, 5])
    # G.add_weighted_edges_from([(0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 2, 4), (1, 3, 5), (2, 3, 6), (2, 4, 7), (2, 5, 8), (3, 4, 9), (3, 5, 10), (4, 5, 11)])

    G.add_nodes_from([0, 1, 2, 3, 4])
    G.add_weighted_edges_from(
        [(0, 1, 1), (0, 2, 1), (0, 3, 2), (0, 4, 3), (1, 2, 2), (1, 3, 2), (1, 4, 3), (2, 3, 3), (2, 4, 2), (3, 4, 2)])
    print(christofides(G))
