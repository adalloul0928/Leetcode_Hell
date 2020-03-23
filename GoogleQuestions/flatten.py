
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next        # right child
        self.child = child      # left child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        self.flatten(head.child)
        self.flatten(head.next)
