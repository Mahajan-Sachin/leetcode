# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    start=None
    def insertion(self,val):
        self.start
        newnode=ListNode(val)
        if not self.start:
            self.start=newnode
        else:
            temp=self.start
            while(temp.next):
                temp=temp.next
            temp.next=newnode

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        temp3=None
        carry=0
        while temp1 or temp2 or carry:
            val1=temp1.val if temp1 else 0
            val2=temp2.val if temp2 else 0
            val=val1+val2+carry
            digit=val%10
            carry=val//10
            self.insertion(digit)
            if temp1: temp1=temp1.next
            if temp2: temp2=temp2.next
        return self.start
