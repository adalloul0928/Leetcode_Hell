class Solution:
    def numIslands(self, grid) -> int:
        if grid:
            rLength = len(grid)
            cLength = len(grid[0])
            count = 0

            for i in range(rLength):
                for j in range(cLength):
                    if grid[i][j] == '1':
                        count += 1
                        self.DFS(grid, i, j)
            return count
        return 0

    def DFS(self, grid, i, j):
        q = []
        q.append([i, j])
        while q:
            curr = q.pop()
            if curr[0] < 0 or curr[1] < 0 or curr[0] == len(grid) or curr[1] == len(grid[0]) or grid[i][j] != '1':
                continue
            else:
                grid[curr[0], curr[1]] = 0
                q.append([i + 1, j])
                q.append([i - 1, j])
                q.append([i, j - 1])
                q.append([i, j + 1])

    def DFSRecursive(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = 0
        self.DFS(grid, i+1, j)
        self.DFS(grid, i-1, j)
        self.DFS(grid, i, j+1)
        self.DFS(grid, i, j-1)