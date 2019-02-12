class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        ˼·������s��ÿһλ������ACSII��ȥ���λ����ֵ��ע����26���ƣ�
        ÿһλ��ֵ��һ�𼴿ɡ�
        """
        n = len(s)
        summ = 0
        for i in range(n):
            summ += (ord(s[i])-ord('A')+1)*pow(26,n-i-1)
        return summ