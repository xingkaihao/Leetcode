class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        思路：总共有m+n-2步，其中向右有m-1步，向下有n-1步，
        因此，求出m+n-2取n-1的组合情况数量即可。
        '''
        a = 1
        for i in range(m+n-2,m-1,-1):
            a *= i
        b = 1
        for j in range(n-1,1,-1):
            b *= j
        return a//b