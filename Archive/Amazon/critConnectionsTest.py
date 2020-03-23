from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections):
        dict = defaultdict(list)
        res = []

        for edge in connections:
            u, v = edge
            dict[u].append(v)
            dict[v].append(u)

        visited = [False for _ in range(n)]
        parent = [float('inf')]*n
        depth = [float('inf')]*n
        lowestVal = [float('inf')]*n
        timer = 0

        def recursiveFind(u):
            nonlocal timer

            depth[u] = timer
            lowestVal[u] = timer
            visited[u] = True

            timer += 1

            for v in dict[u]:
                if not visited[v]:
                    parent[v] = u
                    recursiveFind(v)
                    if lowestVal[v] > depth[u]:
                        res.append([u,v])

                if parent[u] != v:
                    lowestVal[u] = min(lowestVal[u], lowestVal[v])

        recursiveFind(0)
        return res