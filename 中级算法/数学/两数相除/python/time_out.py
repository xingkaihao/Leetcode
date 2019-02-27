class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        思路：直接用除法作弊了。
        """
        flag = 0
        if dividend<0:
            dividend = -dividend
            flag += 1
        if divisor<0:
            divisor = -divisor
            flag += 1
        n = 0
        while dividend>=divisor:
            dividend -= divisor
            n += 1
        n = (-1)**flag * n
        if n >= -2147483648 and n <= 2147483647:
            return n
        else:
            return 2147483647