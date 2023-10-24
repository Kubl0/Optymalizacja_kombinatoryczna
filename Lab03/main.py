class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                print(f"Krawędź {v} -> {i}")
                self.dfs(i, visited)

    def dfs_traversal(self):
        visited = {v: False for v in self.graph}
        for v in self.graph:
            if not visited[v]:
                self.dfs(v, visited)


# Przykład użycia
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("Przeszukiwanie DFS:")
g.dfs_traversal()
