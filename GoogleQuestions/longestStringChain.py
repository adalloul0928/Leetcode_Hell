from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        myDict = defaultdict(int)

        words.sort(key=len)

        totalWords = 0

        for w in words:
            for i in range(len(w)):
                wordChoice = w[:i] + w[i+1:]
                myDict[w] = max(myDict[wordChoice] + 1, myDict[w])
            totalWords = max(myDict[w], totalWords)

        return totalWords