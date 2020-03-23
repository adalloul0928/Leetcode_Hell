class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r = []
        c = []
        for x in range(m):
            for i in range(n):
                if matrix[x][i] == 0:
                    r.append(x)
                    c.append(i)
        for x in r:
            for i in range(n):
                matrix[x][i] = 0

        for x in c:
            for i in range(m):
                matrix[i][x] = 0

    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r = []
        c = []
        for x in range(m):
            for i in range(n):
                if matrix[x][i] == 0:
                    r.append(x)
                    c.append(i)
        for x in r:
            for i in range(n):
                matrix[x][i] = 0

        for x in c:
            for i in range(m):
                matrix[i][x] = 0

sol = Solution()
input = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
sol.setZeroes(input)
for x in input:
    print(x)