# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow.next
        while curr:
            later=curr.next
            curr.next=prev
            prev=curr
            curr=later
        slow.next=None
        t1=head
        t2=prev
        while t2:
            t3=t1.next
            t4=t2.next
            t1.next=t2
            t2.next=t3
            t1=t3
            t2=t4
        