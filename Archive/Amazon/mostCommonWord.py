from collections import Counter
import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        exclude = set(string.punctuation)
        s = ''.join(ch for ch in paragraph if ch not in exclude)
        s = s.lower()
        wordList = s.split(' ')
        bannedDict = {}
        paragraphMax = Counter()

        maxWord = ''
        maxCount = 0

        for word in banned:
            bannedDict[word.lower()] = 1

        for word in wordList:
            if word not in bannedDict:
                paragraphMax[word] += 1
                if paragraphMax[word] > maxCount:
                    maxWord = word
                    maxCount = paragraphMax[word]

        return maxWord

para = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
sol = Solution()
print(sol.mostCommonWord(para, banned))