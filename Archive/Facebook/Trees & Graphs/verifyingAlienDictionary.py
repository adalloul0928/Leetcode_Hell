from collections import defaultdict

class Solution:
    def alienOrder(self, words) -> str:
        lettersDict = defaultdict(list)

        for wordIndex in range(len(words)-1):
            indexLetter = 0
            while words[wordIndex][indexLetter] == words[wordIndex + 1][indexLetter]:
                lettersDict[words[wordIndex][indexLetter]]
                indexLetter += 1
            lettersDict[words[wordIndex][indexLetter]].append(words[wordIndex+1][indexLetter])

        print(lettersDict)

sol = Solution()
input = ['ae', 'ab', 'ba']
sol.alienOrder(input)