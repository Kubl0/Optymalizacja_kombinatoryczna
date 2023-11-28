import networkx as nx


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


def christofides(G):
    if not traingle_inequality(G):
        return Exception("Graph does not satisfy triangle inequality")

    # 1
    T = nx.minimum_spanning_tree(G)

    # 2
    O = [v for v, d in T.degree() if d % 2 == 1]

    M = nx.Graph()
    M.add_nodes_from(O)
    for u in O:
        for v in O:
            if u < v and G.has_edge(u, v):
                M.add_edge(u, v, weight=G[u][v]['weight'])
    M = nx.max_weight_matching(M, maxcardinality=True)

    # 3
    H = nx.MultiGraph(T)
    H.add_edges_from(M)

    # 4
    eulerian_circuit = nx.eulerian_circuit(H)

    # 5
    hamiltonian_circuit = [u for u, v in eulerian_circuit]

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
