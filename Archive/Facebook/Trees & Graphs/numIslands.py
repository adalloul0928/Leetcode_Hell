class Solution:
    def numIslands(self, grid) -> int:
        count = 0
        if not grid:
            return count
        lenRows = len(grid)
        lenCols = len(grid[0])

        def helperCounter(row, col, grid):
            if row < 0 or col < 0 or row > lenRows - 1 or col > lenCols - 1 or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            helperCounter(row + 1, col, grid)
            helperCounter(row, col + 1, grid)
            helperCounter(row - 1, col, grid)
            helperCounter(row, col - 1, grid)

        for row in range(lenRows):
            for col in range(lenCols):
                if grid[row][col] == '1':
                    helperCounter(row, col, grid)
                    count += 1
        return count

sol = Solution()
input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(sol.numIslands(input))