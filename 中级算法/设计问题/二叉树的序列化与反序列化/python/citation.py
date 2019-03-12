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
        思路：递归完成，递归结束的条件是root为空，
        空用符号#表示
        如果root不为空，则把root.val字符化，并加入
        res，并依此递归root.left和root.right。
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
        思路：先把data构建成一个双向序列，
        之后把字符串从头至尾一次输出，
        如果为#则返回None，否则把该数
        整数化并构建成树结构，分别依次
        递归root.left赫尔root.right。
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