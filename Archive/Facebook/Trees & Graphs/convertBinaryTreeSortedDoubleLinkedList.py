
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def treeRecursiveHelper(curr):
            nonlocal last
            nonlocal first
            if curr:
                treeRecursiveHelper(curr.left)
                if last:
                    last.right = curr
                    curr.left = last
                else:
                    first = curr
                last = curr
                treeRecursiveHelper(curr.right)

        if not root:
            return None

        last, first = None, None
        treeRecursiveHelper(root)
        last.right = first
        first.left = last
        return first