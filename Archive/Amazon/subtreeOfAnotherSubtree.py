# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        foundNode = False

        def recursiveFind(s, t):
            if not s or not t:
                return foundNode


# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         startNode = None
#
#         myStack = []
#         secondStack = []
#
#         myStack.append(s)
#
#         while myStack:
#             curr = myStack.pop(0)
#             if curr.val == t.val:
#                 foundNode = True
#                 startNode = curr
#                 break
#             myStack.append(curr.left)
#             myStack.append(curr.right)
#
#         myStack = []
#         myStack.append(curr)
#         secondStack.append(startNode)
#         if startNode:
#             while myStack and secondStack:
#                 currS = myStack.pop(0)
#                 currT = secondStack.pop(0)
#                 if currS.val != currT.val:
#                     return False
#                 myStack.append(currS.left)
#                 myStack.append(currS.right)
#                 secondStack.append(currT.left)
#                 secondStack.append(currT.right)
#
#         if not startNode or myStack or secondStack:
#             return False
#         return True
