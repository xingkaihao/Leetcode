class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        ˼·���׳˵�Ԫ���У�����һ��5���׳˽��ĩβ����һ��0��
        ��ˣ��ͽ׳���5��Ԫ�ظ������ɡ�
        """
        s = 5
        summ = 0
        while n>=s:
            summ += n//s
            s *= 5
        return summ