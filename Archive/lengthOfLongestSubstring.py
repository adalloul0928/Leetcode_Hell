
# OLD SOLUTION
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        # maxSubString = []
        # for x in range(len(s)):
        #     subString = []
        #     i = x
        #     while i < len(s) and s[i] not in subString:
        #         subString.append(s[i])
        #         i += 1
        #     if len(subString) > len(maxSubString):
        #         maxSubString = subString
        # return len(maxSubString)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            maxSubString = 0
            R = 1
            L = 0
            while R < len(s):
                while R < len(s) and s[R] not in s[L:R]:
                    R += 1
                    maxSubString = max(maxSubString, R - L)
                L += 1
            return maxSubString
        else:
            return 1

sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))