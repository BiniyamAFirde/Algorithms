# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
   
            if slow == fast:
             
                pointer1 = head
                pointer2 = slow  
            
                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                
                return pointer1 
        
        return None 
