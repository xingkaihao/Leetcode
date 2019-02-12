class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        思路：阶乘的元素中，存在一个5，阶乘结果末尾就有一个0，
        因此，就阶乘中5的元素个数即可。
        """
        s = 5
        summ = 0
        while n>=s:
            summ += n//s
            s *= 5
        return summ