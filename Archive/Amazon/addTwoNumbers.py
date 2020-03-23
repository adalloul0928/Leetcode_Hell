# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        currNode = ListNode(0)
        head = currNode
        carry = 0
        while l1 != None and l2 != None:
            curr = l1.val + l2.val + carry
            if curr < 10:
                currNode.next = ListNode(curr)
                carry = 0
            else:
                currNode.next = ListNode(curr % 10)
                carry = 1
            l1 = l1.next
            l2 = l2.next
        while l2:
            curr = l2.val + carry
            if curr < 10:
                currNode.next = ListNode(curr)
                carry = 0
            else:
                currNode.next = ListNode(curr % 10)
                carry = 1
            l2 = l2.next
        while l1:
            curr = l1.val + carry
            if curr < 10:
                currNode.next = ListNode(curr)
                carry = 0
            else:
                currNode.next = ListNode(curr % 10)
                carry = 1
            l1 = l1.next
        if carry == 1:
            currNode.next = ListNode(1)
        return head.next