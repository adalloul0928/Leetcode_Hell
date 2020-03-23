class Solution:
    def search(self, nums, target):
        if nums:
            S = 0
            E = len(nums) - 1
            return self.helper(nums, S, E, target)
        else:
            return -1

    def helper(self, nums, S, E, target):
        mid = (S+E)//2
        # print(mid)
        if nums[mid] == target:
            return mid
        if S < E:
            if nums[mid] <= nums[E]:
                if nums[E] >= target >= nums[mid]:
                    return self.helper(nums, mid + 1, E, target)
                else:
                    return self.helper(nums, S, mid - 1, target)
            else:
                if nums[mid] >= target >= nums[S]:
                    return self.helper(nums, S, mid - 1, target)
                else:
                    return self.helper(nums, mid + 1, E, target)
        else:
            return -1

myList = [4,5,6,7,0,1,2]
target = 5
sol = Solution()
for x in range(0,8):
    target = x
    print(x)
    print(sol.search(myList, target))
