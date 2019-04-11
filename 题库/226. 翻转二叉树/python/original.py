# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        ˼·�����ú����ݹ�ȥ������������ķ�ת���ݹ����������rootΪ�գ�
        ����������root
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