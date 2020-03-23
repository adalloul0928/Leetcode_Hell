class Solution:
    def productExceptSelf(self, nums):
        L = []
        R = [0 for x in range(len(nums)-1)]
        lengthNums = len(nums)

        L.append(nums[0])
        R.insert((lengthNums-1), (nums[lengthNums-1]))

        for x in range(1,len(nums)):
            L.append(nums[x] * L[x-1])

        for i in range(lengthNums-2, -1, -1):
            R[i] = nums[i] * R[i+1]

        for n in range(len(nums)):
            if n == 0:
                nums[0] = R[1]
            elif n == len(nums)-1:
                nums[n] = L[len(nums)-2]
            else:
                nums[n] = L[n-1]*R[n+1]
        return nums

sol = Solution()
input = [1,2,3,4]
print(sol.productExceptSelf(input))
