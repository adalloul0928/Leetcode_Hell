class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def recursiveHelper(curr):
            nonlocal serializedStr
            if curr is None:
                serializedStr += "None,"
                return
            else:
                serializedStr += str(curr.val) + ','
                recursiveHelper(curr.left)
                recursiveHelper(curr.right)

        serializedStr = ""
        recursiveHelper(root)
        return serializedStr


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelper(l):
            if l[0] == "None":
                l.pop(0)
                return None
            curr = TreeNode(l[0])
            l.pop(0)
            curr.left = deserializeHelper(l)
            curr.right = deserializeHelper(l)
            return curr

        data_list = data.split(',')
        root = deserializeHelper(data_list)
        return root