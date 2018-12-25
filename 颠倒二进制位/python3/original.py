class Solution:
    # @param n, an integer
    # @return an integer
    '''
    思路：通过format转化成二进制，并转化成列表形式，利用reverse()函数翻转，
    之后利用join把各个二进制的数链接起来，最后返回二进制的整数。
    ''' 
    def reverseBits(self, n):
        l = list('{0:032b}'.format(n))
        l.reverse()
        s = ''.join(l)
        return int(s,2)