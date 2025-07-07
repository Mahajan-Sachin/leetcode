# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1 #example=5
        if n==count:
            return head.next
        temp=head
        val=count-n #5-2=3, it means at index 3, (we want to stop 1 back)
        for i in range(val-1):
            temp=temp.next
        temp.next=temp.next.next
        return head