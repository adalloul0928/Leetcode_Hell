class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rem = 0
        curr = None
        root = None
        curr1 = l1
        curr2 = l2
        while curr1 or curr2:
            if curr1 and curr2:
                total = curr1.val + curr2.val + rem
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                total = curr1.val + rem
                curr1 = curr1.next
            elif curr2:
                total = curr2.val + rem
                curr2 = curr2.next
            temp = ListNode(total % 10)
            rem = total // 10
            if root:
                curr.next = temp
                curr = curr.next
            else:
                root = temp
                curr = temp
        if rem > 0:
            temp = ListNode(rem)
            curr.next = temp
        return root

