# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurseTree(curr):
            if curr == None:
                return False

            rightTree = recurseTree(curr.right)
            leftTree = recurseTree(curr.left)

            mid = curr == p or curr == q

            if mid + leftTree + rightTree >= 2:
                self.ans = curr

            return rightTree or leftTree or mid

        recurseTree(root)
        return self.ans