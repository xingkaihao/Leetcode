class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        思路：用减法代替除法，被除数的绝对值能够减除数绝对值的最大次数即为要求的结果，
        如果直接用减法，会超时。因此嵌套一个循环，每次循环都加倍除数，以此来减少时间。
        """
        sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)  
        a, b = abs(dividend), abs(divisor)  
        ret, c = 0, 0  
  
        while a >= b:  
            c = b  
            i = 0  
            while a >= c:  
                a -= c  
                ret += (1<<i)  
                i += 1  
                c <<= 1  
  
        if sign:  
            ret = -ret  
        return min(max(-2147483648, ret), 2147483647)