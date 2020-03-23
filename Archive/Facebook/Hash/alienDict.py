class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        hashMap = {}
        for x in range(len(order)):
            hashMap[order[x]] = x

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                print(words[i][j])
                print(words[i+1][j])
                if j+1 > len(words[i+1]):
                    return False
                else:
                    if hashMap[words[i][j]] > hashMap[words[i+1][j]]:
                        return False
                    elif hashMap[words[i][j]] == hashMap[words[i+1][j]]:
                        continue
                    else:
                        break
        return True




sol = Solution()
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(sol.isAlienSorted(words, order))
