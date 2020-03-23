class Solution:
    def permuteUnique(self, nums):
        retList = []

        def permuteRecursive(numsSlice, tempList):
            vis = []
            if numsSlice == []:
                    retList.append(tempList)
            else:
                for i in range(len(numsSlice)):
                    r = numsSlice[:]
                    r.pop(i)
                    if numsSlice[i] not in vis:
                        vis += [numsSlice[i]]
                        permuteRecursive(r, tempList + [numsSlice[i]])

        permuteRecursive(nums, [])
        return retList
