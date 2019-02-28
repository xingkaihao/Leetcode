# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        思路：使用递归的方法，首先设置边界条件，当root为空时，返回空列表，
        建立空列表去保存节点值，先递归调用函数，输入root.left，并且和result拼接，
        root的值直接加入到result中，之后递归调用，输入root.right，并且拼接到result中，
        返回result。
        '''
        if root == None:
            return []
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result