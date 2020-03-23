
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        def DFSFlatten(prev, curr):
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            tempNext = curr.next
            tail = DFSFlatten(curr, curr.child)
            curr.child = None
            return DFSFlatten(tail, tempNext)

        if not head:
            return head

        pseudoHead = Node(None, None, head, None)
        DFSFlatten(pseudoHead, pseudoHead.next)
        pseudoHead.next.prev = None
        return pseudoHead.next

