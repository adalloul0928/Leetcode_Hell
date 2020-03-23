class Solution:
    def endArray(self, arr):
        i = 0
        curr = 0
        while i < len(arr) and i >= curr:
            i = max(i, arr[curr] + curr)
            curr += 1
        return i >= len(arr)-1


sol = Solution()
# input = [1,2,0,2,1]
input = [1,2,0,0,1]
print(sol.endArray(input))