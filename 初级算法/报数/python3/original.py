class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        ��n=1��2��ʱ��ֱ������𰸣���n����2��ʱ�򣬶�n-2�Σ�
        ÿ�ζ�ȡ�ķ�ʽΪ������flag����ظ��ַ�����λ�������ظ��ַ���������
        ֮��д����ַ���sts������flag���������ơ�
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        st = "11"
        for i in range(n-2):
            sts = ""
            flag = 0
            for j in range(1, len(st)):
                if st[j] != st[j-1]:
                    num = j-flag
                    s = st[flag]
                    sts += str(num) + s
                    flag = j
                if j ==len(st)-1:
                    num = j - flag + 1
                    s = st[flag]
                    sts += str(num) + s
            st = sts
        return st