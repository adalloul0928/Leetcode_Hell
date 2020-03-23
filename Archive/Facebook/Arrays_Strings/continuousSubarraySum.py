from collections import Counter

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        h = {}
        currSum = 0

        for ind, n  in enumerate(nums):
            currSum += n
            if currSum%k in h and ind > h[currSum%k]:
                return True
            else:
                h[currSum%k] = ind
        return False

sol = Solution()
input = [23, 2, 4, 6, 7]
k = 6
print(sol.checkSubarraySum(input, k))
