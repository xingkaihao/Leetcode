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
        ˼·��������ȱ�����BFS����ͨ������ѭ��Ƕ�ף������ΰ�ÿ��ڵ����q��
        ÿ��ڵ�ֵ����res��ʱ��Ҫע��[]��ʽ��ѭ��ֹͣ�������ǲ�ڵ�ΪNone��
        """
        res = []
        if root == None:
            return res

        q = [root]
        while len(q) != 0:
            res.append([node.val for node in q])
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q

        return res