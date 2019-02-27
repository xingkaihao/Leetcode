class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        ˼·��ͨ��һ���ַ���ȥ����𰸣��ȱ��������ţ����������֣���֮����С�����֡�
        ���������������Ϊ0����û��С����ֱ�ӷ��ؽ��������ʱ���ӷ�ĸ���þ���ֵ��
        �ڼ���С����ʱ���÷�ĸ�Է��ӵ�����*10������ĸ���õ���һλС�����Դ����ƣ�
        һλһλ����С����ͬʱÿ�ζ��Ѹ������Ͷ�Ӧ��ret�������ֵ����ʽ����������
        ������ͬʱ������ȣ��ֵ��д��ڵ�ǰ����ʱ��˵������ѭ���ˣ��ֵ��ж�Ӧ��ret����
        ����ѭ������ʼ�㡣
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