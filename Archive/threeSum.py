# threeSum solution

class Solution:
    def threeSum(self, nums):
        nums.sort()
        A = []
        if len(nums) < 3:
            return []
        else:
            for x in range(len(nums)-2):
                if x == 0 or nums[x] > nums[x-1]:
                    S = x + 1
                    E = len(nums) - 1
                    while S < E:
                        if -nums[x] == (nums[S] + nums[E]):
                            A.append([nums[x], nums[S], nums[E]])
                        if -nums[x] > (nums[S] + nums[E]):
                            currentS = S
                            while nums[currentS] == nums[S] and S < E:
                                S += 1
                        else:
                            currentE = E
                            while nums[currentE] == nums[E] and S < E:
                                E -= 1
        return A


# myList = [-1, 0, 1, 2, -1, -4]
myList = [0,0,0,0]
sol = Solution()
print(sol.threeSum(myList))
