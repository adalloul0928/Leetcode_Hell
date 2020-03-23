# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        myArray = []
        if not root:
            return True

        def isValidHelper(curr):
            if curr == None:
                return
            isValidHelper(curr.left)
            myArray.append(curr.val)
            isValidHelper(curr.right)

        isValidHelper(root)
        for i in range(len(myArray) - 1):
            if myArray[i] >= myArray[i + 1]:
                return False
        return True

sol = Solution()
