# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        retList = []
        if root:
            queue = []
            level = {}
            totalLevels = 0
            queue.append(root)

            retList.append(root.val)
            level[root.val] = 0

            while queue:
                curr = queue.pop(0)
                if curr.right:
                    queue.append(curr.right)
                    level[curr.right.val] = level[curr.val] + 1
                    if level[curr.right.val] > totalLevels:
                        retList.append(curr.right.val)
                        totalLevels += 1
                if curr.left:
                    queue.append(curr.left)
                    level[curr.left.val] = level[curr.val] + 1
                    if level[curr.left.val] > totalLevels:
                        retList.append(curr.left.val)
                        totalLevels += 1
        return retList