class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'(':')', '[':']', '{':'}'}
        for x in s:
            if x in open:
                stack.append(x)
            else:
                if stack and open[stack.pop()] == x:
                    continue
                else:
                    return False
        if stack:
            return False
        return True

mystring = ""
sol = Solution()
print(sol.isValid(mystring))