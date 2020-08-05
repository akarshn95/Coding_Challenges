# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        # serialize in preorder style and converting into a string for easy appending
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return str(root.val) + ',' + left + ',' +right

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # convert string to list
        tree_list = data.split(',')
        # reverse to aid quick pop
        tree_list = tree_list[::-1]
        
        def preorder():
            curr_val = tree_list.pop()
            if curr_val == 'None':
                return
            # reconstruct tree in preorder fashion
            node = TreeNode(int(curr_val))
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
