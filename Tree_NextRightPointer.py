"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def connect_next(node, nextt):
            if not node:
                return None
            node.next = nextt
            connect_next(node.left, node.right)
            connect_next(node.right, node.next.left if node.next else None)
            return node
        return connect_next(root, None)
