from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def eulerian_path(self, u, visited, path):
        for v, w in self.graph[u]:
            if (u, v) not in visited:
                visited.add((u, v))
                visited.add((v, u))
                self.eulerian_path(v, visited, path)
                path.append((u, v, w))

    def chinese_postman(self):
        odd_vertices = [v for v in self.graph if len(self.graph[v]) % 2]
        matching = self.minimum_perfect_matching(odd_vertices)

        for u, v, w in matching:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

        start_vertex = next(iter(self.graph))
        visited, path = set(), []
        self.eulerian_path(start_vertex, visited, path)

        print("Chinese Postman Path:")
        total_weight = sum(w for _, _, w in path)
        for u, v, w in path:
            print(f"{u} -> {v} (Weight: {w})")
        print("Total Weight:", total_weight)

    def minimum_perfect_matching(self, vertices):
        matching, used = [], set()

        for u in vertices:
            if u not in used:
                eligible_edges = [(v, w) for v, w in self.graph[u] if v not in used]
                if eligible_edges:
                    min_edge = min(eligible_edges, key=lambda x: x[1])
                    used.update((u, min_edge[0]))
                    matching.append((u, min_edge[0], min_edge[1]))

        return matching


# Example usage:
g1 = Graph()
g1.add_edge(1, 2, 3)
g1.add_edge(2, 3, 1)
g1.add_edge(3, 1, 2)

g1.chinese_postman()

g2 = Graph()
g2.add_edge(1, 2, 3)
g2.add_edge(2, 3, 1)
g2.add_edge(3, 4, 5)
g2.add_edge(4, 1, 2)

g2.chinese_postman()

