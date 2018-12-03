# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        ˼·����C++һ��
        """
        return root and max(self.maxDepth(root.left), self.maxDepth(root.right))+1 or 0