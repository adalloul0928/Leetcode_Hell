# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        if l2 == None or (l1 and l1.val <= l2.val):
            head = l1
            if l1:
                l1 = l1.next
        else:
            head = l2
            if l2:
                l2 = l2.next
        curr = head
        while l1 or l2:
            if l2 == None or (l1 and l1.val <= l2.val):
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
        return head

