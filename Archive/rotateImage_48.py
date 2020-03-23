class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        visited = []
        for x in range(n*n):
            ind = x
            num = matrix[ind//n][ind%n]
            while ind not in visited:
                visited.append(ind)
                ind = (ind % n) * n + n - 1 - (ind // n)
                tmp = matrix[ind//n][ind%n]
                matrix[ind//n][ind%n] = num
                num = tmp

# input = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

input = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

sol = Solution()
sol.rotate(input)
for x in input:
    print(x)
