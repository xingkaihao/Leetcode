class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        思路：使用了math.factorial求阶乘的函数，
        机器人一共向右走m - 1, 向下走 n - 1, 由组合知识得
        '''
        f = math.factorial
        return int(f(m + n - 2) / f(m - 1) / f(n - 1))