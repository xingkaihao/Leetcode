class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        ˼·���ܹ���m+n-2��������������m-1����������n-1����
        ��ˣ����m+n-2ȡn-1���������������ɡ�
        '''
        a = 1
        for i in range(m+n-2,m-1,-1):
            a *= i
        b = 1
        for j in range(n-1,1,-1):
            b *= j
        return a//b