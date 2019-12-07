from collections import defaultdict

with open('input.txt') as f:
    orbits = f.read().split()


class Graph:
    def __init__(self, data):
        self.graph = defaultdict(list)
        self.path_to_san = set()
        self.path_to_you = set()

        for orbit in data:
            orb = orbit.split(')')
            body = orb[0]
            orbiter = orb[1]

            self.graph[body].append(orbiter)

    def __str__(self):
        return str(self.graph)

    def dfs(self, k='COM', path=[]):
        if k == 'YOU':
            self.path_to_you = set(path)
        if k == 'SAN':
            self.path_to_san = set(path)

        path.append(k)

        for orbit in self.graph[k]:
            self.dfs(orbit, path)

        path.pop()


g = Graph(orbits)
g.dfs()

print(len(g.path_to_san ^ g.path_to_you))
