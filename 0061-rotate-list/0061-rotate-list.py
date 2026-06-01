# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        c=1
        t=head
        while t.next!=None:
            c+=1
            t=t.next
        t.next=head
        k=k%c
        x=c-k
        for i in range(x):
            t=t.next
        nhead=t.next
        t.next=None
        return nhead
        
        