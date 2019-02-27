class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        思路：首先边界条件设置，如果numRows小于s长度或者为1，则直接返回s，
        s分为numRows个层，每层分别放入数组中的不同位置，数组的长度为numRows，
        初始对应位置为''，之后用遍历s，把s中每个字符放到对应的数组位置中，
        idx为数组位置，step控制方向，最后把数组中的字符串都拼接起来。
        """
        if numRows>len(s) or numRows==1:
            return s
        res=['']*numRows
        idx,step=0,1
        for i in s:
            res[idx]+=i
            if idx==0:
                step=1
            elif idx==numRows-1:
                step=-1
            idx+=step
        return ''.join(res)