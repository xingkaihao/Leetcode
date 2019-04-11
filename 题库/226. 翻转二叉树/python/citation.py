# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        思路：因为该函数直接返回root，所以用该函数递归翻转左右子树就可以，
        递归结束条件是root为空。
        '''
        if root == None:
            return root
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root