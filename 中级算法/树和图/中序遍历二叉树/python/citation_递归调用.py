# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        ˼·��ʹ�õݹ�ķ������������ñ߽���������rootΪ��ʱ�����ؿ��б�
        �������б�ȥ����ڵ�ֵ���ȵݹ���ú���������root.left�����Һ�resultƴ�ӣ�
        root��ֱֵ�Ӽ��뵽result�У�֮��ݹ���ã�����root.right������ƴ�ӵ�result�У�
        ����result��
        '''
        if root == None:
            return []
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result