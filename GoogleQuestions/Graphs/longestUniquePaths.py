class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        numCols = len(obstacleGrid[0])
        numRows = len(obstacleGrid)

        for col in range(numCols):
            if obstacleGrid[0][col] == 0:
                obstacleGrid[0][col] = 1
            else:
                obstacleGrid[0][col] = 0

        for row in range(numRows):
            if obstacleGrid[row][0] == 0:
                obstacleGrid[row][0] = 1
            else:
                obstacleGrid[row][0] = 0

        for row in range(1,numRows):
            for col in range(1, numCols):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]

        return obstacleGrid[-1][-1]