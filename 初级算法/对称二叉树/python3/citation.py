# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        思路：root分成左右两支，因为对称，所以L.left和R.right比较，L.right和R.left比较，
        如果两者值相等，递归调用函数，如果不等，返回False。当出现NULL的时候，判断对称位置是否为NULL，返回布尔结果
        """
        if root==None:
            return True
        return self.ValidBST(root.left, root.right)
    
    
    def ValidBST(self, L, R):
        if L==None:
            return R==None
        if R==None:
            return L==None
        if R.val==L.val:
            return self.ValidBST(L.left, R.right) and self.ValidBST(L.right, R.left)
        else:
            return False