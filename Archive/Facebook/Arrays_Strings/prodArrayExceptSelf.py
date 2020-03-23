class Solution:
    def productExceptSelf(self, nums):
        answer = [1]

        for i in range(len(nums)-1):
            answer.append(answer[i]*nums[i])

        i = 1

        for k in reversed(range(len(answer))):
            answer[k] = answer[k] * i
            i *= nums[k]

        return answer

    def productExceptSelf1(self, nums):
        left = [1]
        right = [1]
        answer = []

        for i in range(len(nums)-1):
            left.append(left[i]*nums[i])

        for i in reversed(range(1,len(nums))):
            right.insert(0, nums[i]*right[0])

        for k in range(len(left)):
            answer.append(left[k] * right[k])

        return answer

sol = Solution()
input = [1,2,3,4]
print(sol.productExceptSelf(input))
