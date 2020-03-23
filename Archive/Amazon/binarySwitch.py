class Solution:
    def switchNums(self, input):
        left = 0
        right = len(input)-1
        while left < right:
            while left < right and input[left] == 0:
                left += 1
            while left < right and input[right] == 1:
                right -= 1
            if left < right:
                input[left], input[right] = input[right], input[left]
        return input

input = [1,0,1,1,0,0,0,1,1,0]
sol = Solution()
print(sol.switchNums(input))
