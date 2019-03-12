# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        ˼·���ݹ���ɣ��ݹ������������rootΪ�գ�
        ���÷���#��ʾ
        ���root��Ϊ�գ����root.val�ַ�����������
        res�������˵ݹ�root.left��root.right��
        """
        res = []
        def preOrder(root):
            if not root:
                res.append('#')
            else:
                res.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(res)
    
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        ˼·���Ȱ�data������һ��˫�����У�
        ֮����ַ�����ͷ��βһ�������
        ���Ϊ#�򷵻�None������Ѹ���
        �����������������ṹ���ֱ�����
        �ݹ�root.left�ն�root.right��
        """
        from collections import deque
        tmp = deque(i for i in data.split())
        print(tmp)
        def build():
            if tmp:
                val = tmp.popleft()
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
            return root
        return build()
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))