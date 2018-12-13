class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        思路：把这个问题看成是排列组合问题，当选取一定的2阶台阶，剩下的步数一定是1阶，把问题看成是2阶台阶在
        所有可能位置中的排列组合问题。因此，用for循环取遍2阶所有可能数目，每种可能的数目中求排列组合的所有可能数目，
        这个过程中需要用到阶乘算法，因此自己写了一个阶乘的函数。
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