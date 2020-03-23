import collections

class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(str):
            count = 0
            for char in str:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return ['']

        ret = []
        visited = collections.defaultdict(str)
        visited[s]
        q = collections.deque()
        q.append(s)
        found = False

        while q:
            for i in range(len(q)):
                top = q.popleft()

                if (isValid(top)):
                    found = True
                    ret.append(top)

                if found:
                    continue

                for j in range(len(top)):
                    if top[j] != "(" and top[j] != ")":
                        continue

                    newStr = top[:j] + top[j+1:]

                    if newStr not in visited:
                        visited[newStr]
                        q.append(newStr)
        return ret

# Old Solution
    # def removeInvalidParentheses(self, s: str):
    #     retList = []
    #
    #     def permuteHelper(paranthLeft, build, stack):
    #         if paranthLeft == '':
    #             if stack == []:
    #                 retList.append(build)
    #         else:
    #             if paranthLeft[0] == '(':
    #                 permuteHelper(paranthLeft[1:], build, stack)
    #                 stack.append('(')
    #                 permuteHelper(paranthLeft[1:], build + "(", stack)
    #             elif paranthLeft[0] == ")":
    #                 permuteHelper(paranthLeft[1:], build, stack)
    #                 if stack:
    #                     stack.pop()
    #                     permuteHelper(paranthLeft[1:], build + ')', stack)
    #
    #     permuteHelper(s, '', [])
    #     return retList

sol = Solution()
input = "()())()"
print(sol.removeInvalidParentheses(input))