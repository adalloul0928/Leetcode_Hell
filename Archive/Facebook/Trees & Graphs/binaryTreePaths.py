# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        retList = []

        def recurseTree(curr, path):
            if curr:
                path += str(curr.val)
                if not curr.left and not curr.right:
                    retList.append(path)
                path += "->"
                recurseTree(curr.left, path)
                recurseTree(curr.right, path)

        recurseTree(root, "")
        return retList
