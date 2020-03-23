from collections import Counter

class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        retArray = []
        L = 0
        R = len(nums) - 1
        mydict = Counter()
        for i in nums:
            mydict[i] += 1

        mydict[nums[L]] -= 1
        mydict[nums[R]] -= 1

        while L < R:
            if mydict[(nums[L] + nums[R])*-1] > 0:
                print("L: {}, R: {}, L + R: {}".format(nums[L], nums[R], (nums[L] + nums[R])*-1))
                # print(mydict)
                retArray.append([nums[L], nums[R], (nums[L] + nums[R])*-1])
                R -= 1
                mydict[nums[R]] -= 1
            elif nums[L] + nums[R] > 0:
                R -= 1
                mydict[nums[R]] -= 1
            elif nums[L] + nums[R] <= 0:
                L += 1
                mydict[nums[L]] -= 1
        return retArray

sol = Solution()
input = [1,2,-2,-1]
print(sol.threeSum(input))


