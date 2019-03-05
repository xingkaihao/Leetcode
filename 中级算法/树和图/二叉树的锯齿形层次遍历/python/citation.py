# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        ˼·���Ѷ�������ÿһ���еĽڵ����һ���б��ú��������б����б��еķǿ�
        ����������һ���б��Դ����ƣ����ܰѶ�������ÿ���б�ͳ�Ƴ�����������һ��flag
        ȥ�������˳�򼴿ɣ�ÿ����һ��flagȡ����
        '''
        if not root:return []
        q = [root]
        res = []
        flag = -1
        while q:
            flag = -flag
            tmp=[]
            q2 = []
            for i in q:
                tmp.append(i.val)
                if i.left:
                    q2.append(i.left)
                if i.right:
                    q2.append(i.right)
            res.append(tmp[::flag])
            q=q2
        return res