class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        思路：x和y通过异或得到使不同的位置置“1”，bin（）转化为二进制，str.count()计算“1”的个数。
        """
        return bin(x^y).count("1")