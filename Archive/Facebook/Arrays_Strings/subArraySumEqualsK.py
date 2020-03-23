from collections import Counter

class Solution:
    def subarraySum(self, nums, k) -> int:
        counter = 0
        hashMap = Counter()
        hashMap[0] += 1
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            if currSum - k in hashMap:
                counter += hashMap[currSum - k]
                hashMap[currSum - k] += 1
            else:
                hashMap[currSum] += 1
        return counter

nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))