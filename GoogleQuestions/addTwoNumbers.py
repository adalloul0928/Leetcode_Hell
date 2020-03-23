# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        curr1 = l1
        curr2 = l2
        sumReturn = []
        while curr1 or curr2:
            if not curr1:
                sumReturn.insert(0, curr2.val + carry)
                carry = 0
            elif not curr2:
                sumReturn.insert(0, curr1.val + carry)
                carry = 0
            else:
                if curr1.val + curr2.val > 9:
                    sumReturn.insert(0, curr1.val + curr2.val % 10)
                    carry = 1
                else:
                    sumReturn.insert(0, curr1.val + curr2.val)
        return str(sumReturn)