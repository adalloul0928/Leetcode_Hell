class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums:
            f = 0
            for x in range(len(nums)):
                f = max(f, x + nums[x])
                if x >= f:
                    break
            return f >= len(nums)-1
        return False