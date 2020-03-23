class Solution:
    def longestIncreasingPath(self, matrix) -> int:

        resultMaxPath = 0

        if not matrix:
            return resultMaxPath

        cols = len(matrix[0])
        rows = len(matrix)

        DP = [[1 for _ in range(cols)] for _ in range(rows)]

        for indRow in range(rows):
            for indCol in range(cols):
                top = indRow - 1
                bottom = indRow + 1
                left = indCol -  1
                right = indCol + 1
                if top >= 0 and matrix[indRow][indCol] > matrix[top][indCol]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[top][indCol] + 1)
                if bottom < rows and matrix[indRow][indCol] > matrix[bottom][indCol]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[bottom][indCol] + 1)
                if left >= 0 and matrix[indRow][indCol] > matrix[indRow][left]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[indRow][left] + 1)
                if right < cols and matrix[indRow][indCol] > matrix[indRow][right]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[indRow][right] + 1)
                resultMaxPath = max(resultMaxPath, DP[indRow][indCol])

        DP = [[1 for _ in range(cols)] for _ in range(rows)]

        for indRow in range(rows):
            for indCol in range(cols):
                top = indRow - 1
                bottom = indRow + 1
                left = indCol - 1
                right = indCol + 1
                if top >= 0 and matrix[indRow][indCol] < matrix[top][indCol]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[top][indCol] + 1)
                if bottom < rows and matrix[indRow][indCol] < matrix[bottom][indCol]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[bottom][indCol] + 1)
                if left >= 0 and matrix[indRow][indCol] < matrix[indRow][left]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[indRow][left] + 1)
                if right < cols and matrix[indRow][indCol] < matrix[indRow][right]:
                    DP[indRow][indCol] = max(DP[indRow][indCol], DP[indRow][right] + 1)
                resultMaxPath = max(resultMaxPath, DP[indRow][indCol])

        print(DP)
        return resultMaxPath

input = [[7,8,9],[9,7,6],[7,2,3]]
sol = Solution()
print(sol.longestIncreasingPath(input))