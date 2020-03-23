import copy

class Solution:
    def permute(self, nums):
        returnList = []

        def DFS(remain, stack):
            if remain == []:
                returnList.append(stack[:])
            else:
                for i in range(len(remain)):
                    r = copy.copy(remain)
                    s = r.pop(i)

                    DFS(r, stack + [s])

        DFS(nums, [])
        return returnList

sol = Solution()
input = [1,2,3]
print(sol.permute(input))

