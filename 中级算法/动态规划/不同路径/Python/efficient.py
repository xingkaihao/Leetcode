class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        ˼·��ͬ��������������Ŀ��������һ��ѭ����������ˣ����
        C^(m-1)_(m+n-2)
        '''
        res = 1
        for i in range(m, m+n-1):
            res *= i
            res /= i-m+1
        return int(res)