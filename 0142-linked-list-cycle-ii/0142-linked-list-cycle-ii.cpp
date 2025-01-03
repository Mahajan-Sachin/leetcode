class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) return nullptr; // No cycle if list is empty or has only one node

        ListNode *slow = head, *fast = head;

        // Detect if there is a cycle
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) { // Cycle detected
                // Reset one pointer to head
                ListNode *entry = head;
                while (entry != slow) {
                    entry = entry->next;
                    slow = slow->next;
                }
                return entry; // Cycle starts here
            }
        }

        return nullptr; // No cycle
    }
};
