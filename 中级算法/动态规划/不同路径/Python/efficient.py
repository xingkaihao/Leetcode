class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        思路：同样是求组合情况数目，不过用一个循环就求出来了，很妙，
        C^(m-1)_(m+n-2)
        '''
        res = 1
        for i in range(m, m+n-1):
            res *= i
            res /= i-m+1
        return int(res)