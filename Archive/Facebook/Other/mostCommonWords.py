from collections import Counter


def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # WRITE YOUR CODE HERE

    bannedWords = set(wordsToExclude)
    for char in "!?;,'.":
        literatureText = literatureText.replace(char, ' ')
    allWords = literatureText.lower().split()
    myDict = Counter()
    highestCount = 0
    retList = []
    for word in allWords:
        if word not in bannedWords:
            myDict[word] += 1
            highestCount = max(highestCount, myDict[word])

    for word, countWord in myDict.items():
        if countWord >= highestCount:
            retList.append(countWord)

    return retList

paragraph = "Jack and jill went to the hill jack"
bannedwords = ['and', 'the', 'went']
print(retrieveMostFrequentlyUsedWords(paragraph, bannedwords))