class Solution:
    def toLowerCase(self, str: str) -> str:
        '''
        ˼·������ACSIIת����Сд��
        '''
        res = ''
        n = ord('a')-ord('A')
        for i in str:
            if ord(i)<=ord('Z') and ord(i)>=ord('A'):
                res += chr(ord(i)+n)
            else:
                res += i
        return res