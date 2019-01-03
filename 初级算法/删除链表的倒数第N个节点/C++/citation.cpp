/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 和python的思路基本一致，不过C++不允许指针指向NULL，
 * 需要处理各种出现NULL的情况。
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head == NULL) return head;
        if(head->next == NULL){
            return NULL;
        } 
        ListNode* fast = head;
        ListNode* slow = head;
        for(int i=0; i<n; ++i){
            fast = fast->next;
        }
        if(fast == NULL){
            head = head->next;
            return head;
        }
        while(fast->next){
            fast = fast->next;
            slow = slow->next;        
        }
        slow->next = slow->next->next;
        return head;
    }
};