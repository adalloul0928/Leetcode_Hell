class Solution:
    def numIslands(self, grid) -> int:
        def numIslands(self, grid: List[List[str]]) -> int:
            def BFSHelper(row, col):
                q = []
                q.append((row, col))
                while q:
                    curr = q.pop()
                    currRow = curr[0]
                    currCol = curr[1]
                    if currRow >= 0 and currRow < len(grid) and currCol >= 0 and currCol < len(grid[0]) and \
                            grid[currRow][currCol] == '1':
                        q += (
                        (currRow + 1, currCol), (currRow - 1, currCol), (currRow, currCol + 1), (currRow, currCol - 1))
                        grid[currRow][currCol] = '0'

            counter = 0

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == '1':
                        BFSHelper(row, col)
                        counter += 1
            return counter


