# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        思路：把二叉树的每一层中的节点放入一个列表，让后遍历这个列表，把列表中的非空
        子树放入另一个列表，以此类推，就能把二叉树的每层列表统计出来，另外用一个flag
        去控制输出顺序即可，每到下一层flag取反。
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