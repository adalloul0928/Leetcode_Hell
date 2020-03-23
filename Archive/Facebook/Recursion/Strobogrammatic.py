class Solution:
    def findStrobogrammatic(self, n: int):
        retList = []
        myDict = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}

        for x in range(10**(n-1)-1, 10**n):
            tempNum = str(x)
            compNum = ''
            if tempNum[0] in myDict:
                for i in tempNum:
                    if i not in myDict:
                        break
                    compNum = myDict[i] + compNum
                if tempNum == compNum:
                    retList.append(compNum)
        return retList

sol = Solution()
input = 2
print(sol.findStrobogrammatic(input))