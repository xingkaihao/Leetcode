# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        思路：使用二分查找，当start和end移动到相邻的时候，判断start和end哪个为True
        输出为True的那个
        """
        start = 1
        end = n
        while end-start > 1:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
                
        if isBadVersion(start):
            return start
        else:
            return end