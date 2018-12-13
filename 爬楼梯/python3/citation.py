class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        ˼·����������⿴��������������⣬��ѡȡһ����2��̨�ף�ʣ�µĲ���һ����1�ף������⿴����2��̨����
        ���п���λ���е�����������⡣��ˣ���forѭ��ȡ��2�����п�����Ŀ��ÿ�ֿ��ܵ���Ŀ����������ϵ����п�����Ŀ��
        �����������Ҫ�õ��׳��㷨������Լ�д��һ���׳˵ĺ�����
        """
        num = 1
        for i in range(1, n//2+1):
            num = num + self.factorial((n-i))//(self.factorial((n-i-i)) * self.factorial(i))
        return num
    
    
    def factorial(self, n):
        m = 1
        for i in range(1, n+1):
            m = m*i
        return m