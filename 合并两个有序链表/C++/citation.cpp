/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 思路和python和一样，但是需要先确定head的当前和next不为NULL。
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL) return l2;
        else if(l2 == NULL) return l1;
        ListNode *head;
        ListNode *first;
        if(l1->val < l2->val){
            head = l1;
            l1 = l1->next;
        }
        else{
            head = l2;
            l2 = l2->next;
        }
        first = head; 
        while(l1 && l2 ){
            if(l1->val < l2->val){
                head->next = l1;
                l1 = l1->next;
            }
            else{
                head->next = l2;
                l2 = l2->next;
            }
            head = head->next;
        }
        if(l1 == NULL) head->next =l2;
        else if(l2 == NULL) head->next = l1;
        return first;
    }
};