class Solution:
    def fibBottomUp(self, n):
        memo = [1,1]

        if n <=1:
            return memo[n]

        for i in range(2,n+1):
            memo.append(memo[i-1] + memo[i-2])

        return memo[n]

sol = Solution()
input = 10
print(sol.fibBottomUp(input))