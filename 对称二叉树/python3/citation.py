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
        ˼·��root�ֳ�������֧����Ϊ�Գƣ�����L.left��R.right�Ƚϣ�L.right��R.left�Ƚϣ�
        �������ֵ��ȣ��ݹ���ú�����������ȣ�����False��������NULL��ʱ���ж϶Գ�λ���Ƿ�ΪNULL�����ز������
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