# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    思路：通过递归把二叉树中的所有值保存在一个列表中，然后把列表排序，
    返回列表对应值即可。
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = self.recursion(root)
        result.sort()
        return result[k-1]
    def recursion(self,root):
        if root == None:
            return []
        return [root.val]+self.recursion(root.right)+self.recursion(root.left)