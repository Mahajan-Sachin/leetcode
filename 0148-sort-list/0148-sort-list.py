# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis=[]
        temp=head
        while temp:
            lis.append(temp.val)
            temp=temp.next
        lis.sort()
        temp=head
        for value in lis:
            temp.val=value
            temp=temp.next
        return head

