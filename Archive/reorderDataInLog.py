# NOT FINISHED!

class Solution:
    def reorderLogFiles(self, logs):
        i = 0
        arr = logs.split()
        words = []
        nums = []
        for x in arr:
            if x[0] == d:
                nums.append(x)
            else:
                tempWords = x.split()
                for j in words:
                    for z in tempWords[1]:
                        if tempWords[1][z] > words[]
                words.append(x)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
print(sol.reorderLogFiles(logs))
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]