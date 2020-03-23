class Solution:
    def twoSum(self, nums, target: int):
        mydict = {}
        for ind, num in enumerate(nums):
            difTarget = target - num
            if difTarget in mydict:
                return [mydict[difTarget], ind]
            mydict[num] = ind

sol = Solution()
arry = [2, 7, 11, 15]
target = 26
print(sol.twoSum(arry, target))