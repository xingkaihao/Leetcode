/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * ˼·��pythonһ��
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(root==NULL) return true;
        return ValidBST(root->left, root->right);
    }
    bool ValidBST(TreeNode* L, TreeNode* R){
        if(L==NULL) return R== NULL;
        if(R==NULL) return L==NULL;
        if(R->val==L->val) return ValidBST(L->left, R->right) && ValidBST(L->right, R->left);
        else return false;
    }
};