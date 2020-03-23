import copy

class Solution:
    def subsets(self, nums):
        returnList = [[]]

        def DFS(curr, numtemp):
            if curr == []:
                return
            else:
                for i in range(len(curr)):
                    r = copy.copy(numtemp)
                    r.append(curr[i])
                    returnList.append(r)
                    DFS(curr[i+1:], r)

        DFS(nums, [])
        return returnList

sol = Solution()
input = [1,2,3]
print(sol.subsets(input))