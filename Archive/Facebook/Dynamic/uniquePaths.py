class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store = [[x for x in range(n)] for x in range(m)]

        for c in range(n):
            store[0][c] = 1

        for r in range(m):
            store[r][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                store[row][col] = store[row-1][col] + store[row][col-1]

        return store[m-1][n-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        store = [[0 for x in range(n)] for x in range(m)]

        for c in range(n):
            store[0][c] = 1

        for r in range(m):
            store[r][0] = 1

        def uniquePathRecurse(row, col):
            if row == 0 or col == 0:
                return store[row][col]
            elif store[row][col] > 0:
                return store[row][col]
            else:
                store[row][col] = uniquePathRecurse(row-1, col) + uniquePathRecurse(row, col-1)
                return store[row][col]

        uniquePathRecurse(m-1, n-1)
        return store[m-1][n-1]

sol = Solution()
row = 3
col = 2
input = [row, col]
print(sol.uniquePaths2(*input))