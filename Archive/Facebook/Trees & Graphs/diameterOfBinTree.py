# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxDiameter = 0

        def recurseHelper(curr):
            nonlocal maxDiameter
            if curr:
                if not curr.left and not curr.right:
                    return 0
                LTree = 0
                RTree = 0
                if curr.left:
                    LTree = 1 + recurseHelper(curr.left)
                if curr.right:
                    RTree = 1 + recurseHelper(curr.right)
                sumTree = LTree + RTree
                if sumTree > maxDiameter:
                    maxDiameter = sumTree
                return max(LTree, RTree)

        recurseHelper(root)
        return maxDiameter


    # SOLUTION #2
    def diameterOfBinaryTree2(self, root):
        self.ans = 1

        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1