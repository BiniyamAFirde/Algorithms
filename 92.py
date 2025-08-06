# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        dummy=ListNode(0,head)
        leftPrev,curr=dummy,head
        for i in range(left-1):
            leftPrev,curr=curr,curr.next
        prev=None
        for i in range(left-right+1):
            tempNext=curr.next
            curr.next=prev
            prev,curr=curr,tempNext
        leftPrev.next.next=curr
        leftPrev.next=prev
        return dummy.next 
        """

        if not head or left == right:
            return head
            
        dummy = ListNode(0, head)
        left_prev = dummy
        curr = head
        
        # Move to the starting position (left-1)
        for i in range(left - 1):
            left_prev = curr
            curr = curr.next
        
        # Reverse the sublist from left to right
        prev = None
        for i in range(right - left + 1):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        # Connect the reversed sublist back
        left_prev.next.next = curr
        left_prev.next = prev
        
        return dummy.next
