class Solution:
    # @param n, an integer
    # @return an integer
    '''
    ˼·��ͨ��formatת���ɶ����ƣ���ת�����б���ʽ������reverse()������ת��
    ֮������join�Ѹ��������Ƶ���������������󷵻ض����Ƶ�������
    ''' 
    def reverseBits(self, n):
        l = list('{0:032b}'.format(n))
        l.reverse()
        s = ''.join(l)
        return int(s,2)