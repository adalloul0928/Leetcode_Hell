from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            L = 0
            R = 0
            longestSubString = 0
            mydict = Counter()
            while R < len(s):
                mydict[s[R]] += 1
                while mydict[s[R]] > 1:
                    mydict[s[L]] -= 1
                    L += 1
                R += 1
                longestSubString = max(longestSubString, R - L)
            return longestSubString
        return 0

sol = Solution()
input = "pwwkew"
print(sol.lengthOfLongestSubstring(input))
