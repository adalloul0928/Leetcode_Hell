class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        for i, x in enumerate(nums):
            if (target - x) in hashtable:
                return [hashtable[target - x],i]
            else:
                hashtable[x] = i
        return False

mylist = 2,7,11,15
target = 9
mySol = Solution()
print (mySol.twoSum(mylist, target))
