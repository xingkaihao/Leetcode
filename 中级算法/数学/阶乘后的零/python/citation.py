class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        思路：阶乘元素中存在一个5，阶乘结果末尾就会有一个0，求n中5的因素个数即可
        """
        ret = 0
        while n != 0:
            ret += n //5
            n //= 5
        return ret