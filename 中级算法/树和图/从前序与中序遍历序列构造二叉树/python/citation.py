# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        ˼·��preorder�еĵ�һ���ڵ�һ��Ϊ���ڵ㣬inorder�ж�Ӧ�Ľڵ����Ϊ��������
        �ұ�Ϊ���������õݹ鷽�����Դ����ƣ��ݹ麯������root���ݹ����Ϊ����Ϊ��
        '''
        if len(preorder)==0:
            return None
        root = TreeNode(preorder[0])
        n = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:n+1], inorder[:n])
        root.right = self.buildTree(preorder[n+1:], inorder[n+1:])
        return root