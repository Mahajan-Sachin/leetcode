/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count=0;
        ListNode* temp=head;
        while(temp){
            temp=temp->next;
            count++;
        }
        temp=head;
        int pos=count-n;
        if(pos==0){
            ListNode* curr=head->next;
            delete temp;
            return curr;
        }
        else {
            ListNode* temp=head;
            for(int i=0;i<pos-1;i++){
                temp=temp->next;
            }
            temp->next=temp->next->next;
        }
        return head;
    }
};