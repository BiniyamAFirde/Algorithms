# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast=slow=dummy
        for i in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next

        '''
        curr=head
        b=0
        c=0
        next_node=curr.next
        while curr:
            curr=curr.next
            b+=1
            curr=next_node
        while curr:
            curr=curr.next
            c+=1
            if c == b-n:
                curr=curr.next
            curr=next_node
        return head
        '''
