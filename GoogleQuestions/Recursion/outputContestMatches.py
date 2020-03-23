class Solution:
    def findContestMatch(self, n: int) -> str:
        def recurseMatches(lowSeed, highSeed):
            if lowSeed >= highSeed:
                return
            curr = (str(lowSeed), str(highSeed))
            return "(" + str(recurseMatches(lowSeed, highSeed)) + "," + str(recurseMatches(lowSeed, highSeed) + ")"

        highSeed = 1
        lowSeed = n
