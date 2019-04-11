# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        ˼·����Ϊ�ú���ֱ�ӷ���root�������øú����ݹ鷭ת���������Ϳ��ԣ�
        �ݹ����������rootΪ�ա�
        '''
        if root == None:
            return root
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root