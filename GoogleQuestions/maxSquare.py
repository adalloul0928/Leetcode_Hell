class Solution:
    def maximalSquare(self, matrix) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dpArray = [[0 for _ in range(col+1)] for _ in range(row+1)]
        maxSquare = 0

        for r in range(row):
            dpArray[r][0] = int(matrix[r][0])

        for c in range(col):
            dpArray[0][c] = int(matrix[0][c])

        for r in range(1, row+1):
            for c in range(1, col+1):
                if matrix[r-1][c-1] == '1':
                    dpArray[r][c] = min(dpArray[r - 1][c], dpArray[r][c - 1], dpArray[r - 1][c - 1]) + 1
                maxSquare = max(maxSquare, dpArray[r][c])
        return maxSquare*maxSquare

sol = Solution()
input = [["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"]]
# input = [['1']]
print(sol.maximalSquare(input))