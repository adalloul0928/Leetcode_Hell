from collections import deque
from collections import defaultdict

class Solution:
    def shortestDistance(self, grid) -> int:
        minDist = float('inf')
        numRows = len(grid)
        numCols = len(grid[0])

        for r in range(numRows):
            for c in range(numCols):
                # print("*****************************")
                # print("Row: {}, Col: {}".format(r, c))
                if grid[r][c] != 0:
                    continue

                tmpSum = 0
                level = 0

                queue = deque()
                visited = defaultdict(list)

                queue.append((r, c))

                while queue:
                    tmpList = []
                    # print("LEVEL: {}".format(level))
                    for i in range(len(queue)):
                        curr = queue.pop()
                        if curr[0] >= 0 and curr[1] >= 0 and curr[0] < numRows and curr[1] < numCols:
                            node = curr[0] * numCols + curr[1]
                            if node not in visited:
                                # print("Row: {}, Col: {}".format(curr[0],curr[1]))
                                if grid[curr[0]][curr[1]] == 0:
                                    tmpList.append((curr[0] + 1, curr[1]))
                                    tmpList.append((curr[0] - 1, curr[1]))
                                    tmpList.append((curr[0], curr[1] + 1))
                                    tmpList.append((curr[0], curr[1] - 1))
                                elif grid[curr[0]][curr[1]] == 1:
                                    tmpSum += level
                                    # print(tmpSum)
                                visited[node]
                                # print("Visited: {}".format(visited))
                    queue = tmpList
                    level += 1

                if tmpSum > 0 and tmpSum < minDist:
                    minDist = tmpSum
        return minDist

sol = Solution()
input = [
    [1,0,2,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]]
# input = [
#     [0,0,1],
#     [0,0,0],
#     [1,0,0],
# ]
# input = [
#     [0,1],
#     [0,0],
# ]
print(sol.shortestDistance(input))