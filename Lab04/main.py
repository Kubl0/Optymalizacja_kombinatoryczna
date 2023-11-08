class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim(self):
        parent = [-1] * self.vertices
        key = [float('inf')] * self.vertices
        key[0] = 0
        mst_set = [False] * self.vertices

        for _ in range(self.vertices):
            min_key = float('inf')
            u = -1
            for v in range(self.vertices):
                if not mst_set[v] and key[v] < min_key:
                    min_key = key[v]
                    u = v

            mst_set[u] = True

            for v in range(self.vertices):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.display_mst(parent)

    def display_mst(self, parent):
        print("Prim's Algorithm >> ")
        total_weight = 0
        for v in range(1, self.vertices):
            print(f"Edge {parent[v]} - {v}, Weight: {self.graph[v][parent[v]]}")
            total_weight += self.graph[v][parent[v]]
        print(f"Total Weight: {total_weight}")


g = Graph(5)
g.add_edge(1, 0, 2)
g.add_edge(3, 0, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim()
