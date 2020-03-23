class Solution:
    def maxSubArray(self, nums) -> int:
        max_curr = max_glob = nums[0]
        for i in range(1,len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            if max_curr > max_glob:
                max_glob = max_curr
        return max_glob


myarray = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()
print(sol.maxSubArray(myarray))