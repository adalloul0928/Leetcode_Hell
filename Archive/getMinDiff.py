from collections import Counter

class Solution:
    def getMinimumDifference(self, a, b):
        retList = []
        for x in range(len(a)):
            if len(a[x]) != len(b[x]):
                retList.append(-1)
            else:
                word1 = a[x]
                word2 = b[x]
                c = 0
                lettersMap = Counter()

                for i in range(len(word1)):
                    lettersMap[word1[i]] += 1

                for j in range(len(word2)):
                    if word2[j] in lettersMap:
                        lettersMap[word2[j]] -= 1
                        if lettersMap[word2[j]] == 0:
                            del lettersMap[word2[j]]
                    else:
                        c += 1
                retList.append(c)
        return retList

sol = Solution()
a = ['abc', 'aaa']
b = ['bba', 'bbb']
print(sol.getMinimumDifference(a, b))