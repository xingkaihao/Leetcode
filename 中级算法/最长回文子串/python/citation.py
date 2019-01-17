class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        maxl为最长回文子串的首位长度差，初始为0，start是最长回文子串的首部位置，初始为0，
        回文字符串分为两种情况，一种是奇数个字符，一种是偶数个字符，所以分为两种情况判断，
        本方法最开始寻找的是最长回文子串的中间部分，也就是最小对称部分，找到这个部分之和，
        随着i的增大，逐渐去增加回文子串的头尾，直到找到最长子串，如果存在多个回文子串也没有
        问题，maxl能够保留到更长的回文子串，直到寻找的到最长的。
        """
        n = len(s)
        maxl = 0
        start = 0
        if n < 2 or s == s[::-1]: return s
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]