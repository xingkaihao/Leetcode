class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        ˼·��������Կ����ǰ��ַ������·����numRows�����У�
        ��������һ���ֵ�ȥ�ֲ㣬���ǲ�������ֵ�Ǹò��Ӧ���ַ�����
        ֮�����s�е�ÿ���ַ����Ѹ��ַ��ŵ���Ӧ���ֵ���У���direct
        ȥ���Ʒ����������в��ַ���ƴ�ӵ�һ��
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