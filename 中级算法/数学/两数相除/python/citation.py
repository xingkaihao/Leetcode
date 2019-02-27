class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        ˼·���ü�������������������ľ���ֵ�ܹ�����������ֵ����������ΪҪ��Ľ����
        ���ֱ���ü������ᳬʱ�����Ƕ��һ��ѭ����ÿ��ѭ�����ӱ��������Դ�������ʱ�䡣
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