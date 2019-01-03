/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 思路：采用递归调用，如果root为空，返回0，如果不为空，向左右分别搜索，
 * 每搜索一次，返回值加一，直到root为空。
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        return root ? max(maxDepth(root->left),maxDepth(root->right))+1 : 0;
    }
};