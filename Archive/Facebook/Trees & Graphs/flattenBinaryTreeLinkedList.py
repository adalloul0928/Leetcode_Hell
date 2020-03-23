# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            myArray = []

            def preOrder(curr):
                if curr == None:
                    return
                myArray.append(curr)
                preOrder(curr.left)
                preOrder(curr.right)

            preOrder(root)
            for i in range(len(myArray) - 1):
                myArray[i].left = None
                myArray[i].right = myArray[i + 1]

    def flatten2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            myArray = []

            def preOrder(curr):
                if curr == None:
                    return
                curr.right =
                preOrder(curr.left)
                preOrder(curr.right)
