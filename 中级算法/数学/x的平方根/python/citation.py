class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        思路：最小二乘法
        """
        if x<=1:
            return x
        l = 0
        r = 50000
        while(l<r):
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid>x:
                r=mid
            else:
                l = mid+1
        return l-1