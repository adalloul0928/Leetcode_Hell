class Solution:
    def maxProfit(self, prices) -> int:
        maxProfit = 0
        p1 = 0
        p2 = 1

        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
                p2 = p2+1
            else:
                if prices[p2] - prices[p1] > maxProfit:
                    maxProfit = prices[p2] - prices[p1]
                p2 += 1
        return maxProfit

sol = Solution()
input = [7,1,5,3,6,4]
print(sol.maxProfit(input))