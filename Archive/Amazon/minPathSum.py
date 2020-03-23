class Solution:
    def minPathSum(self, grid) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        newGrid = [[0 for x in range(colLen)] for y in range(rowLen)]

        newGrid[0][0] = grid[0][0]
        for ind in range(1, colLen):
            newGrid[0][ind] = newGrid[0][ind-1] + grid[0][ind]

        for ind in range(1, rowLen):
            newGrid[ind][0] = newGrid[ind-1][0] + grid[ind][0]

        for r in range(1,rowLen):
            for c in range(1, colLen):
                newGrid[r][c] = min(newGrid[r-1][c], newGrid[r][c-1]) + grid[r][c]

        return newGrid[-1][-1]

sol = Solution()
input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(sol.minPathSum(input))