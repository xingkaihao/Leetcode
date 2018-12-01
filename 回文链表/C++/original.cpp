/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 思路和python一样
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head==NULL || head->next == NULL ) return true;
        vector<int> temp;
        int n=0;
        while(head){
            n += 1;
            temp.push_back(head->val);
            head = head->next;
        }
        for(int i=0; i<n; ++i){
            if(temp[i] != temp[n-i-1]) return false;
        }
        return true;
    }
};