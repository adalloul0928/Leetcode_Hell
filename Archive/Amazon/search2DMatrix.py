class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowSize = len(matrix)
        colSize = len(matrix[0])
        p = [rowSize-1, 0]

        while p[0] >= 0 and p[1] < colSize:
            print(p)
            if matrix[p[0]][p[1]] == target:
                return True
            if matrix[p[0]][p[1]] > target:
                p[0] -= 1
            elif matrix[p[0]][p[1]] < target:
                p[1] += 1
        return False

sol = Solution()
input = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print(sol.searchMatrix(input, target))