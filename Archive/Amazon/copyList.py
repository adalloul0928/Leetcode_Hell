# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        visited = {}

        def recursiveCall(curr):
            nonlocal visited
            if curr == None:
                return None
            elif curr in visited:
                return visited[curr]
            newNode = Node(curr.val, None, None)
            visited[curr] = newNode
            newNode.next = recursiveCall(curr.next)
            newNode.random = recursiveCall(curr.random)
            return newNode

        copyHead = recursiveCall(head)
        return copyHead