from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not wordList or not beginWord or not endWord:
            return 0
        resultLength = 1

        dictWords = defaultdict(list)
        visitedWords = defaultdict()

        for word in wordList:
            for ind in range(len(word)):
                keyWord = word[:ind] + "*" + word[ind+1:]
                dictWords[keyWord].append(word)

        Q = [beginWord]

        while Q:
            tempQ = []
            print(Q)
            for word in Q:
                if word == endWord:
                    return resultLength

                if word in visitedWords:
                    continue
                visitedWords[word] = 1
                for ind in range(len(word)):
                    keyWord = word[:ind] + "*" + word[ind+1:]
                    if keyWord in dictWords:
                        tempQ += dictWords[keyWord]
                        del dictWords[keyWord]
            resultLength += 1
            Q = tempQ

        return 0

sol = Solution()
arr = ["hot","dot","dog","lot","log","cog"]
beg = "hit"
end = "cog"
print(sol.ladderLength(beg, end, arr))