# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together 
# the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tmp = ListNode()

        while l1:
            if not l2:
                tmp.next = l1
                break
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
                continue

            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next

        if l2:
            tmp.next = l2

        return head.next
            

        
        
                
                
            
        
        
            
        
                
