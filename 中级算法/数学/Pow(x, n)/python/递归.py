class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        思路：使用递归
        """
        if (n==0):
            return 1
        if(n<0):
            x=1/x
        n = abs(n)
        A = self.myPow(x,n//2)
        if(n%2==0):
            return A*A
        else:
            return A*A*x