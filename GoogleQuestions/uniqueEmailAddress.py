class Solution:
    def numUniqueEmails(self, emails) -> int:
        # r = set()
        # for i in emails:
        #     a = True
        #     p = True
        #     temp = ""
        #     for j in i:
        #         if j == "+":
        #             p = False
        #         if j == "@":
        #             temp += j
        #             a = False
        #         elif j != "." and p and a:
        #             temp += j
        #         elif not a:
        #             temp += j
        #     r.add(temp)
        # return len(r)

        r = set()
        for e in emails:
            l, d = e.split("@")
            if "+" in l:
                l = l[:l.index("+")]
            l = l.replace('.','')
            r.add(l + "@" + d)
        return len(r)


input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
sol = Solution()
print(sol.numUniqueEmails(input))