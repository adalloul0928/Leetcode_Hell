# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

class Solution2:

    def reverseListHelper(self, head, prev):
        if head == None:
            return prev
        result = self.reverseListHelper(prev, head.next)
        head.next = prev
        return result

    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            self.reverseListHelper(head, None)
        else:
            return None

sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
sol.reverseList(node1)