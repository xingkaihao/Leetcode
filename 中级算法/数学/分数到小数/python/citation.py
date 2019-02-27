class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        思路：通过一个字符串去保存答案，先保存正负号，是整数部分，再之后是小数部分。
        如果两个数的余数为0，则没有小数，直接返回结果。计算时分子分母都用绝对值。
        在计算小数的时候，用分母对分子的余数*10整除分母，得到第一位小数，以此类推，
        一位一位的求小数，同时每次都把该余数和对应的ret长度以字典的形式保存起来，
        余数相同时，商相等，字典中存在当前余数时，说明出现循环了，字典中对应的ret长度
        就是循环的起始点。
        """
        if denominator == 0:
            return
        
        ret = ''
        if numerator // denominator < 0:
            ret += '-'
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ret += str(numerator // denominator)
        ret += '.'
        
        numerator %= denominator
        i = len(ret)  
        table = {}
        
        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i 
            else:   
                i = table[numerator]
                return ret[:i] + '('+ ret[i:] +')'
            numerator *= 10
            ret += str(numerator // denominator)
            numerator %= denominator
            i += 1
            
        return ret