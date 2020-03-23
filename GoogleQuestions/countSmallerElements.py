import bisect

class Solution:
    def countSmaller(self, nums):
        if not nums:
            return 0

        newArr = []
        result = []
        for num in nums[::-1]:
            ind = bisect.bisect_left(newArr, num)
            newArr.insert(ind, num)
            result.append(ind)
        return result[::-1]


sol = Solution()
# input = [-1, -1]
input = [5,2,6,1]
print(sol.countSmaller(input))
