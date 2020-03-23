class Solution:
    def twoSum(self, nums, target: int):
        mydict = {}
        for i, x in enumerate(nums):
            dif = target - x
            if dif in mydict:
                return [mydict[dif], i]
            mydict[x] = i
