class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        ˼·���׳�Ԫ���д���һ��5���׳˽��ĩβ�ͻ���һ��0����n��5�����ظ�������
        """
        ret = 0
        while n != 0:
            ret += n //5
            n //= 5
        return ret