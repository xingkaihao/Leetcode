class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        ˼·��ʹ����math.factorial��׳˵ĺ�����
        ������һ��������m - 1, ������ n - 1, �����֪ʶ��
        '''
        f = math.factorial
        return int(f(m + n - 2) / f(m - 1) / f(n - 1))