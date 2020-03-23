class Solution:
    def spiralOrder(self, matrix):
        returnList = []
        k = 0               # starting row index
        l = 0               # starting column index
        r = len(matrix)     # ending row index
        c = len(matrix[0])  # ending column index

        while k < r and l < c:
            for x in range(k,c):
                returnList.append(matrix[k][x])

            k += 1

            for i in range(l+1, r):
                returnList.append(matrix[i][c-1])

            c -= 1

            if k < r:
                for j in range(c, l, -1):
                    returnList.append(matrix[r-1][j-1])

                r -= 1

            if l < c:
                for h in range(r, k, -1):
                    returnList.append(matrix[h-1][l])
                l += 1

        return returnList


# input = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

input = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.spiralOrder(input))