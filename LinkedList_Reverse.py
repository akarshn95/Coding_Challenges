# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use temp to swap node nexts an prev to store previous value
        node = head
        prev=None
        temp=None
        # store in temp to traverse the LL
        while node:
            temp=node.next
            node.next=prev
            prev=node
            node=temp
        head=prev
        
        return head
    
     def reverseList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        new_node = ListNode()
        new_node = self.reverseList_recursive(head.next)
        
        head.next.next = head
        head.next = None
        return new_node
        

    
