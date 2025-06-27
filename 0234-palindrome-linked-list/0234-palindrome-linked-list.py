# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True
        temp=head
        List=[]
        while(temp):
            List.append(temp.val)
            temp=temp.next
        return List==List[::-1]

        