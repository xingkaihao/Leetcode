class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        当n=1或2的时候，直接输入答案，当n大于2的时候，读n-2次，
        每次读取的方式为：利用flag标记重复字符的首位，数出重复字符的数量，
        之后写入空字符串sts，更新flag，依此类推。
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        st = "11"
        for i in range(n-2):
            sts = ""
            flag = 0
            for j in range(1, len(st)):
                if st[j] != st[j-1]:
                    num = j-flag
                    s = st[flag]
                    sts += str(num) + s
                    flag = j
                if j ==len(st)-1:
                    num = j - flag + 1
                    s = st[flag]
                    sts += str(num) + s
            st = sts
        return st