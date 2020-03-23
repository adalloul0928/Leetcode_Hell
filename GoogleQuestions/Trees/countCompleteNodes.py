# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = []
        stack.append(root)
        countLevels = 0
        numLeaves = 0
        nullFound = False

        while stack:
            tempStack = []
            if not nullFound:
                countLevels += 1
            for node in stack:
                if node.left and node.right:
                    tempStack.append(node.left)
                    tempStack.append(node.right)
                if node.left and not node.right:
                    tempStack.append(node.left)
                    numLeaves += len(tempStack)
                    break
            stack = tempStack

        return (2**countLevels + numLeaves - 1)