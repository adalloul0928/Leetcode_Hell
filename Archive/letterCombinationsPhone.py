class Solution:
    def letterCombinations(self, digits):

        mapping = {'1': [''], '2': ['a','b','c'], '3': ['d', 'e', 'f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
                   '8': ['t','u','v'], '9': ['w','x','y','z'], '0': ['']}

        def combineStuff(currList, mapping, digit):
            tempList = []

            for x in currList:
                for i in mapping[digit]:
                    tempList.append(x+i)
            return tempList

        if digits == []:
            return []

        result = ['']

        for i in digits:
            result = combineStuff(result, mapping, i)

        return result

sol = Solution()
input = "23"
print(sol.letterCombinations(input))