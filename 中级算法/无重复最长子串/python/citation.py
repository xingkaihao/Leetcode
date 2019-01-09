class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        r = 0 

        for v in s:
            if v not in tmp:
                tmp += v
            else:
                n = tmp.index(v)
                tmp = tmp[n+1:] + v
            r = max(len(tmp), r)
        return r 