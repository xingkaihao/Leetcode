class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        思路：遍历s的每一位，利用ACSII码去求该位的数值，注意是26进制，
        每一位数值加一起即可。
        """
        n = len(s)
        summ = 0
        for i in range(n):
            summ += (ord(s[i])-ord('A')+1)*pow(26,n-i-1)
        return summ