# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float('-inf')

        def maxHelper(curr):
            nonlocal maxSum
            if curr == None:
                return 0
            leftGain = max(maxHelper(curr.left), 0)
            rightGain = max(maxHelper(curr.right), 0)

            path = curr.val + leftGain + rightGain

            maxSum = max(path, maxSum)

            return curr.val + max(leftGain, rightGain)

        maxHelper(root)
        return maxSum
