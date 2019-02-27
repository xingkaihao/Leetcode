class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        思路：本题可以看成是把字符串重新分配成numRows个层中，
        可以利用一个字典去分层，键是层数，键值是该层对应的字符串，
        之后遍历s中的每个字符，把该字符放到对应的字典层中，用direct
        去控制方向，最后把所有层字符串拼接到一起。
        '''
        if numRows == 1:
            return s
        dic = {}
        for i in range(numRows):
            dic[i] = ''
        flag = 0
        direct = 0
        for j in s:
            if direct==0:
                if flag<numRows:
                    dic[flag] += j
                    flag += 1
                else:
                    direct = 1
                    dic[flag-2] += j
                    flag -= 3
            else:
                if flag>=0:
                    dic[flag] += j
                    flag -= 1
                else:
                    direct = 0
                    dic[flag+2] += j
                    flag += 3
        ss=''
        for k in range(numRows):
            ss += dic[k]
        return ss