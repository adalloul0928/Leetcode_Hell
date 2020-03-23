# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        def recurseTree(node, nextNode, currMax):
            if not nextNode:
                return currMax
            if nextNode.val - node.val == 1:
                return max(recurseTree(nextNode, nextNode.left, currMax + 1), recurseTree(nextNode, nextNode.right, currMax + 1))
            else:
                return max(recurseTree(nextNode, nextNode.left, 1), recurseTree(nextNode, nextNode.right, 1), currMax)

        return max(recurseTree(root, root.left, 1), recurseTree(root, root.right, 1))

input = [1,2,3,4,5]