class Solution:
    def trap(self, height) -> int:
        totalHeight = 0
        if not height:
            return totalHeight
        leftMax = [0 for x in range(len(height))]
        rightMax = [0 for x in range(len(height))]
        leftMax[0] = height[0]
        rightMax[len(height) - 1] = height[len(height) - 1]
        for ind in range(1, len(height)):
            leftMax[ind] = max(height[ind], leftMax[ind - 1])
        for ind in reversed(range(0, len(height) - 1)):
            rightMax[ind] = max(height[ind], rightMax[ind + 1])

        for ind in range(len(height)):
            tempWater = min(leftMax[ind], rightMax[ind])
            if tempWater > height[ind]:
                totalHeight += tempWater - height[ind]
        return totalHeight

input = [5,4,1,2]
sol = Solution()
print(sol.trap(input))