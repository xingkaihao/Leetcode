/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 思路和python的广度优先遍历一样。
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root == NULL) return res;
        vector<TreeNode*> q;
        q.push_back(root);
        while(q.size()!=0){
            vector<int> p;
            for(int i=0; i<q.size(); ++i){
                p.push_back(q[i]->val);
            }
            res.push_back(p);
            vector<TreeNode*> new_q;
            for(int j=0; j<q.size(); ++j){
                if(q[j]->left) new_q.push_back(q[j]->left);
                if(q[j]->right) new_q.push_back(q[j]->right);
            }
            q=new_q;
        }
        return res;
    }
};