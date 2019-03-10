# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    ˼·��ͨ���ݹ�Ѷ������е�����ֵ������һ���б��У�Ȼ����б�����
    �����б��Ӧֵ���ɡ�
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = self.recursion(root)
        result.sort()
        return result[k-1]
    def recursion(self,root):
        if root == None:
            return []
        return [root.val]+self.recursion(root.right)+self.recursion(root.left)