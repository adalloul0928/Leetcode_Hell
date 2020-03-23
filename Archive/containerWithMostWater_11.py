class Solution:
    def maxArea(self, height) -> int:
        L = 0
        R = len(height)-1
        maxWater = min(height[L], height[R]) * (R - L)
        while L < R:
            if height[L] > height[R]:
                R -= 1
                maxWater = max(maxWater, min(height[L],height[R]) * (R - L))
            else:
                L += 1
                maxWater = max(maxWater, min(height[L],height[R]) * (R - L))
        return maxWater

array = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(array))