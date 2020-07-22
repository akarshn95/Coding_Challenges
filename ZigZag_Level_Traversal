# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return None
        level=[root]
        res=[[root.val]]
        # i to keep track of alternative levels
        i=1
        
        while level:
            queue=[]
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # next level is the queue of children
            level=queue
            # break if there are no further levels
            if not level:
                break
            
            # next level is to be reversed if i is odd
            if i%2!=0:
                res.append(nodes.val for nodes in reversed(level))
            else:
                res.append(nodes.val for nodes in level)
            i+=1
            
        return res
