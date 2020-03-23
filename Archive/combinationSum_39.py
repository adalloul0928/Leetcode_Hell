class Solution:
    def combinationSum(self, candidates, target):

        def combHelper(currSum, currList, mainList):
            for i in range(len(mainList)):
                if mainList[i] + currSum > target:
                    return
                elif currSum + mainList[i] == target:
                    sol.append(currList + [mainList[i]])
                    return
                else:
                    combHelper(currSum + mainList[i], currList + [mainList[i]], mainList[i:])

        sol = []
        combHelper(0, [], sorted(candidates))

        return sol


candidates = [2,3,6,7]
target = 7

# candidates = [2,3,5]
# target = 8

mysol = Solution()
print(mysol.combinationSum(candidates, target))