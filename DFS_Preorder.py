# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        
        while True:
            # this loops implements DFS to go as deep as possible
            while root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            if not stack:
                return res
            #backtrack
            node=stack.pop()
            root=node.right
            
                  
