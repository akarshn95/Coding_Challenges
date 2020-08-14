# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists):
        heap = []
        # convert all the nodes to a heap
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next
        
        dummy = node = ListNode(0)
        
        while heap:
            node_val = heapq.heappop(heap)
            node.next = ListNode(node_val)
            node = node.next
        return dummy.next
            
