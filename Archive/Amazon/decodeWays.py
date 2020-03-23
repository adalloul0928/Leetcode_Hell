class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1

        if int(s[0]) >= 1:
            dp[1] = 1
        else:
            dp[1] = 0

        for ind in range(2, len(s)+1):
            oneDig = int(s[ind-1])
            twoDig = int(s[ind-2:ind])
            if oneDig >= 1:
                dp[ind] += dp[ind-1]
            if twoDig >= 10 and twoDig <= 26:
                dp[ind] += dp[ind-2]
        return dp[len(s)]

input = '12'
sol = Solution()
print(sol.numDecodings(input))