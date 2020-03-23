from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections):
        res = []
        g = defaultdict(list)
        for con in connections:
            u, v = con
            g[u].append(v)
            g[v].append(u)

        depth = [float('inf') for _ in range(n)]
        lowest = [float('inf') for _ in range(n)]
        parent = [float('inf') for _ in range(n)]
        visited = [False for _ in range(n)]
        timer = 0

        def recursiveFind(u):
            nonlocal timer

            depth[u] = timer
            lowest[u] = timer
            visited[u] = True

            timer += 1

            for v in g[u]:
                if visited[v] == False:
                    parent[v] = u
                    recursiveFind(v)
                    if lowest[v] > depth[u]:
                        res.append([u, v])

                if parent[u] != v:
                    lowest[u] = min(lowest[u], lowest[v])

        recursiveFind(0)
        return res

input = [[0,1],[1,2],[2,0],[1,3]]
n = 4
sol = Solution()
sol.criticalConnections(n, input)