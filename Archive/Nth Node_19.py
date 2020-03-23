# Nth node from the end of a linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        curr = head
        prevN = head
        while curr != None:
            if i > n:
                prevN = prevN.next
            curr = curr.next
            i += 1
        if i >= n:
            if prevN.next == None:
                head = None
            elif prevN == head and i == n:
                head = head.next
            else:
                prevN.next = prevN.next.next
        return head