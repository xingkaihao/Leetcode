# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        思路：新定义一个函数，用该函数的递归去解决问题。该函数的输入有root、small、large，root分别同时向左右两个方向递归，
        递归的停止条件是搜索到叶子节点完毕。验证二叉树的方法是，判断左子节点值小于根节点，且右子节点值大于根节点值，遍历整个
        二叉树均满足此条件，则为验证成果。
        """
        return self.ValidBST(root, -2**32, 2**32-1)
    
    
    def ValidBST(self, root, small, large):
        if root==None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.ValidBST(root.left, small, root.val) and self.ValidBST(root.right, root.val, large)