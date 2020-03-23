# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSumHelper(self, root, tempSum):
        if root == None:
            return float("-inf")
        else:
            maxL = self.maxPathSum(root.left)
            maxR = self.maxPathSum(root.right)
            currMax = max(0, root.val, root.val + maxL.val + maxR.val, root.val + maxL.val, root.val + maxR.val)
            return currMax

    def maxPathSum(self, root):
        tempSum = 0
        val = self.maxPathSumHelper(root, tempSum)
