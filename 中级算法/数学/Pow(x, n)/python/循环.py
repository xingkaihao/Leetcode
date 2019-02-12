
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        思路：使用平方的方法去实现乘方
        """
        result=1
        if n<0:
            n=-n
            flag=1
        else:
            flag=0
        while n>0:
            if n%2==1:
                result=result*x
            x=x*x
            n//=2
        if flag==0:
            return result
        else:
            return 1.0/result