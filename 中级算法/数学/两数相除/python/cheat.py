class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        ˼·��ֱ���ó��������ˡ�
        """
        n = dividend/divisor
        if n <= 2147483647 and n>=-2147483648:
            return int(n)
        else:
            return 2147483647