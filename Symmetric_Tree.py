# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        def symmetric_nodes(node_a, node_b):
            
            if not node_a and not node_b:
                return True
            
            if not node_a or not node_b:
                return False
            
            if node_a.val!=node_b.val:
                return False
            
            return symmetric_nodes(node_a.left, node_b.right) and symmetric_nodes(node_a.right, node_b.left)
        
        return symmetric_nodes(root.left, root.right)
