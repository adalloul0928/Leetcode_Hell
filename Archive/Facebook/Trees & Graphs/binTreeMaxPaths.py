class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxRecursiveHelper(curr):
            nonlocal maxSum
            if not curr:
                return 0

            leftMax = max(maxRecursiveHelper(curr.left),0)
            rightMax = max(maxRecursiveHelper(curr.right),0)

            new_path = curr.val + leftMax + rightMax

            maxSum = max(new_path, maxSum)
            return curr.val + max(leftMax, rightMax)

        maxSum = float('-inf')
        maxRecursiveHelper(root)
        return maxSum