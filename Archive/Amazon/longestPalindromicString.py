class Solution:
    def longestPalindrome(self, s: str) -> str:
        myArr = [[0 for x in range(len(s))] for x in range(len(s))]
        start = 0
        maxPalindrome = 0

        for x in range(len(s)):
            myArr[x][x] = 1
            maxPalindrome = 1
            start = x

        # two letters in a row
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                myArr[i][i+1] = 1
                maxPalindrome = 2
                start = i

        # three letters in a row
        for j in range(len(s)):
            for i in range(len(s)):
                if i < j:
                    if s[i] == s[j] and myArr[i + 1][j - 1] == 1:
                        myArr[i][j] = True
                        if j - i + 1 > maxPalindrome:
                            maxPalindrome = j - i + 1
                            start = i
        return s[start:start+maxPalindrome]

sol = Solution()
input = 'babbbbad'
print(sol.longestPalindrome(input))