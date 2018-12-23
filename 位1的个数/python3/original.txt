class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        思路：把n转化成二进制字符串，遍历这个字符串，计算字符串中‘1’的个数
        """
        num = 0
        for i in '{:b}'.format(n):
            if i=='1':
                num += 1
        return num