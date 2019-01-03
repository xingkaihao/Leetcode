/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 思路和python程序完全一样
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL) return head;
        ListNode* temp0 = NULL;
        ListNode* temp1 = head;
        ListNode* temp2 = head->next;
        while(temp2){
            temp1->next = temp0;
            temp0 = temp1;
            temp1 = temp2;
            temp2 = temp2->next;
        }
        temp1->next = temp0;
        head = temp1;
        return head;
    }
};