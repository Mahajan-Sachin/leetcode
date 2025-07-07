# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        node1=head
        val=count-k
        for i in range(k-1):
            node1=node1.next
        node2=head
        for i in range(val):
            node2=node2.next
        node1.val,node2.val=node2.val,node1.val
        return head


        