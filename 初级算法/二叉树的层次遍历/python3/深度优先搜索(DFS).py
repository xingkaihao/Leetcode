# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        ˼·�����������������DFS����ͨ���ݹ���ã���ÿ��ڵ��ֵ��������Ӧ��λ�ã�
        ���ú�����depth���ƽڵ�洢λ�ã��ݹ�ֹͣ��������rootΪNone��
        """
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if root == None:
            return res
        if len(res) < depth+1:
            res.append([])
        res[depth].append(root.val)
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)