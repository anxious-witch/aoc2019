from collections import defaultdict

with open('input.txt') as f:
    orbits = f.read().split()


class Graph:
    def __init__(self, data):
        self.graph = defaultdict(list)
        self.orbits = 0

        for orbit in data:
            orb = orbit.split(')')
            body = orb[0]
            orbiter = orb[1]

            self.graph[body].append(orbiter)

    def __str__(self):
        return str(self.graph)

    def dfs(self, k, dist=1):
        self.orbits += dist * len(self.graph[k])

        for orbit in self.graph[k]:
            self.dfs(orbit, dist + 1)


g = Graph(orbits)
g.dfs('COM')
print(g.orbits)
