class Solution(object):
    def postorderTraversal(self, root):
        res, stack = [ ], [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        # do root, right, left traversal and reverse it 
        return reversed(res)
        
    
        
        
      
