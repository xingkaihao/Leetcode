class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        思路：先找到haystack中和needle首字母相同的位置，然后haystack从该位置开始，
        needle长度的字符串和needle匹配，如果一样就输出0.
        """
        # 先求出needle长度
        n = len(needle)
        # 对于本题而言，当needle是空字符串时我们应当返回0。这与C语言的strstr()以及Java的indexOf()定义相符
        if needle == "":
            return 0
        
        for i in range(len(haystack) - n + 1):
            if haystack[i] == needle[0] and haystack[i:i+n] == needle:
                return i
            
        return -1
