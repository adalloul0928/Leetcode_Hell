class Solution:
    def maxArea(self, height) -> int:
        maxWater = 0
        L = 0
        R = len(height) - 1
        while R > L:
            maxWater = max(maxWater, min(height[L], height[R]) * (R - L))
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return maxWater

input = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(input))