class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        思路：把strs的第一个字符串设置为比较字符temp，
        去分别和strs中的每个字符串比较，两个字符串比较过程中，
        以较短的字符串为标准，分别比较字符串中的每个字符是否一致，
        如果出现不一致，就把temp中从不一致的字符开始，
        删除后面所有字符，跳出本次循环，
        如果两个字符比较的循环结束了还没有出现不一致，
        就把temp的长度取成该循环的长度。
        """
        if not len(strs):
            return ""
        temp = strs[0]
        for i in strs:
            if not len(i):
                return ""
            for j in range(min(len(i),len(temp))):
                if temp[j] != i[j]:
                    temp = temp[:j]
                    break
                if j+1 == min(len(i),len(temp)):
                    temp = temp[:j+1]
        return temp