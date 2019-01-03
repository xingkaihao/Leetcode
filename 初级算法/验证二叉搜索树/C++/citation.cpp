/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 思路和python一样，注意INT64_MIN=-2^32、INT64_MAX=2^32-1，以及long数据类型的使用。
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return ValidBST(root, INT64_MIN, INT64_MAX);
    }
    bool ValidBST(TreeNode* root, long small, long large){
        if(root==NULL) return true;
        if(small >= root->val || large <= root->val) return false;
        return ValidBST(root->left, small, root->val) && ValidBST(root->right, root->val, large);
    }
};