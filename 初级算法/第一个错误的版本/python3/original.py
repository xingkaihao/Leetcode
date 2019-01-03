# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        ˼·��ʹ�ö��ֲ��ң���start��end�ƶ������ڵ�ʱ���ж�start��end�ĸ�ΪTrue
        ���ΪTrue���Ǹ�
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