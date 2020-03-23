class Solution:
    def letterCombinations(self, digits):
        digitsMap = {"0":[], "1":[],
                     "2":['a','b','c'],
                     "3":['d','e','f'],
                     "4":['g','h','i'],
                     "5":['j','k','l'],
                     "6":['m','n','o'],
                     "7":['p', 'q', 'r', 's'],
                     "8":['t', 'u', 'v'],
                     "9":['w', 'x', 'y', 'z'],
                     }
        retList = []

        def helperFunc(input, templist):
            if input == "":
                retList.append(templist)
            else:
                for i in range(len(digitsMap[input[0]])):
                    helperFunc(input[1:], templist + digitsMap[input[0]][i])

        helperFunc(digits, "")
        return retList

sol = Solution()
input = "23"
print(sol.letterCombinations(input))