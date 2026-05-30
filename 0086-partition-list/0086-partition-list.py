# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1=ListNode(-1)
        d2=ListNode(-1)
        t1=d1
        t2=d2
        t3=head
        while t3:
            if t3.val<x:
                t1.next=t3
                t1=t1.next
                t3=t3.next
            else:
                t2.next=t3
                t2=t2.next
                t3=t3.next
        t2.next=None
        t1.next=d2.next
        return d1.next