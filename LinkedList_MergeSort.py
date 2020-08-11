# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       
        def mergeSort(head):
            if not head or not head.next:
                return head

            left = slow = fast = head   # pointers to help split the list
            fast = fast.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            right = slow.next       # next of left is the right half
            slow.next = None        # this splits the list into two
            
            left_s = mergeSort(left)
            right_s = mergeSort(right)
            return merge(left_s, right_s)
        
        def merge(l1, l2):
            dummy = ListNode(-1)
            prev = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            
            prev.next = l1 or l2         # add any remaining elements
            return dummy.next
        
        return mergeSort(head)
            
