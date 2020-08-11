# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[sum] = 1
        
        def dfs(node,curr):
            if not node:
                return
            curr += node.val
            self.total += self.lookup[curr]
            self.lookup[curr+sum]+=1   
            dfs(node.left,curr)
            dfs(node.right,curr)
            self.lookup[curr+sum]-=1
            
        dfs(root,0)
        return self.total
