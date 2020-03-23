from collections import defaultdict, Counter

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        if numCourses == 0:
            return []

        G = defaultdict(list)
        numEdges = Counter()
        for x in range(numCourses):
            numEdges[x] = 0
        Q = []
        result = []

        for class1, prereq in prerequisites:
            G[prereq] += [class1]
            numEdges[class1] += 1

        for num in numEdges:
            if numEdges[num] == 0:
                Q += [num]

        while Q:
            curr = Q.pop(0)
            result.append(curr)
            for neighbor in G[curr]:
                numEdges[neighbor] -= 1
                if numEdges[neighbor] == 0:
                    Q.append(neighbor)

        if len(result) == numCourses:
            return result

        return []


sol = Solution()
input = [[0,1],[0,2],[1,2]]
numCourses = 3
print(sol.findOrder(numCourses, input))


