class Solution:
    # Space complexity of O(n * m)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for x in range(n)] for i in range(m)]
        for i in range(1,m):
            for x in range(1,n):
                dp[i][x] = dp[i-1][x] + dp[i][x-1]
        return dp[-1][-1]

    # Space complexity of O(n)
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1 for x in range(n)]
        for i in range(1,m):
            for x in range(1,n):
                dp[x] = dp[x] + dp[x-1]
        return dp[-1]

m, n = 3, 2
sol = Solution()
print(sol.uniquePaths2(m, n))