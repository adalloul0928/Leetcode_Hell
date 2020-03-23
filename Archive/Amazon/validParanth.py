class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftParanth = ['(', '{', '[']
        for x in s:
            if x in leftParanth:
                stack.append(x)
            else:
                if x == ')':
                    if not stack or stack.pop() != '(':
                        return False
                elif x == "}":
                    if not stack or stack.pop() != '{':
                        return False
                else:
                    if not stack or stack.pop() != "[":
                        return False
        if not stack:
            return True
        else:
            return False

input = "()}"
sol = Solution()
print(sol.isValid(input))