class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        #λ����
        no_carry_sum=a^b#a��b����λʱ�ĺͣ�ǡ�����������һ��
        carry=(a&b)<<1#a��b�ĺ͵Ľ�λ��ǡ���������������һλ
        return sum([no_carry_sum,carry])#ǰ����֮��