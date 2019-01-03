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
        ˼·���¶���һ���������øú����ĵݹ�ȥ������⡣�ú�����������root��small��large��root�ֱ�ͬʱ��������������ݹ飬
        �ݹ��ֹͣ������������Ҷ�ӽڵ���ϡ���֤�������ķ����ǣ��ж����ӽڵ�ֵС�ڸ��ڵ㣬�����ӽڵ�ֵ���ڸ��ڵ�ֵ����������
        ���������������������Ϊ��֤�ɹ���
        """
        return self.ValidBST(root, -2**32, 2**32-1)
    
    
    def ValidBST(self, root, small, large):
        if root==None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.ValidBST(root.left, small, root.val) and self.ValidBST(root.right, root.val, large)