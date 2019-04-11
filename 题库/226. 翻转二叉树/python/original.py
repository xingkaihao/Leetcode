# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        思路：利用函数递归去完成左右子树的翻转，递归结束条件是root为空，
        主函数返回root
        '''
        if root == None:
            return root
        self.invert(root)
        return root
    
    def invert(self, root):
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)