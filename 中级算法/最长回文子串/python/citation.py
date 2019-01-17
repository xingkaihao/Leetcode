class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        maxlΪ������Ӵ�����λ���Ȳ��ʼΪ0��start��������Ӵ����ײ�λ�ã���ʼΪ0��
        �����ַ�����Ϊ���������һ�����������ַ���һ����ż�����ַ������Է�Ϊ��������жϣ�
        �������ʼѰ�ҵ���������Ӵ����м䲿�֣�Ҳ������С�ԳƲ��֣��ҵ��������֮�ͣ�
        ����i��������ȥ���ӻ����Ӵ���ͷβ��ֱ���ҵ���Ӵ���������ڶ�������Ӵ�Ҳû��
        ���⣬maxl�ܹ������������Ļ����Ӵ���ֱ��Ѱ�ҵĵ���ġ�
        """
        n = len(s)
        maxl = 0
        start = 0
        if n < 2 or s == s[::-1]: return s
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]