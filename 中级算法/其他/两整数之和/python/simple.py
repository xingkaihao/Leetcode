class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        思路：使用sum()函数
        注意：sum操作的对象中必须有可迭代对象
        """
        return sum([a,b])