class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        depth=0
        level=[root] if root else []
        
        while level:
            queue=[]
            depth+=1
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # scan the next level nodes in next iteration; queue is empty when it goes to last level        
            level=queue
            
        return depth
