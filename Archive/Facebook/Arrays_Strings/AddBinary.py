class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        while y != 0:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    def addBinary2(self, a: str, b: str) -> str:
        carry = 0
        ret = []
        aLength = len(a)-1
        bLength = len(b)-1
        while aLength >= 0 and bLength >= 0:
            if int(a[aLength]) + int(b[bLength]) == 2:
                ret.append(str(carry))
                carry = 1
            elif int(a[aLength]) + int(b[bLength]) == 1:
                if carry == 1:
                    ret.append('0')
                else:
                    ret.append('1')
            else:
                ret.append(str(carry))
                carry = 0
            aLength -= 1
            bLength -= 1
        while aLength >= 0:
            curr = int(a[aLength]) + carry
            if curr == 2:
                ret.append('0')
                carry = 1
            elif curr == 1:
                ret.append('1')
                carry = 0
            else:
                ret.append('0')
            aLength -= 1

        while bLength >= 0:
            curr = int(b[bLength]) + carry
            if curr == 2:
                ret.append('0')
                carry = 1
            elif curr == 1:
                ret.append('1')
                carry = 0
            else:
                ret.append('0')
            bLength -= 1
        if carry == 1:
            ret.append(str(carry))
        ret.reverse()
        return "".join(ret)

strA = '11'
strB = '1'
sol = Solution()
print(sol.addBinary(strA, strB))