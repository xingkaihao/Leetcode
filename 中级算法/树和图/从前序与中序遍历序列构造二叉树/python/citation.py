# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        思路：preorder中的第一个节点一定为根节点，inorder中对应的节点左边为左子树，
        右边为右子树，用递归方法，以此类推，递归函数返回root，递归出口为子树为空
        '''
        if len(preorder)==0:
            return None
        root = TreeNode(preorder[0])
        n = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:n+1], inorder[:n])
        root.right = self.buildTree(preorder[n+1:], inorder[n+1:])
        return root