class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        def recurseHelper(curr, currDepth):
            nonlocal maxDepth
            if not curr:
                return
            recurseHelper(curr.left, currDepth + 1)
            maxDepth = max(maxDepth, currDepth)
            recurseHelper(curr.right, currDepth + 1)

        maxDepth = 0

        if not root:
            return 0
        else:
            recurseHelper(root, 1)
        return maxDepth

    def maxDepth2(self, root: TreeNode) -> int:
        maxDepth = 0
        q = []
        q.append(root)

        while q:
            maxDepth += 1
            tempList = []
            for i in range(len(q)):
                curr = q.pop()
                if curr.left:
                    tempList.append(curr.left)
                if curr.right:
                    tempList.append(curr.right)
            q = tempList
        return maxDepth


