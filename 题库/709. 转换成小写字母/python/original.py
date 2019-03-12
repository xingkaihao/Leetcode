class Solution:
    def toLowerCase(self, str: str) -> str:
        '''
        思路：利用ACSII转换大小写。
        '''
        res = ''
        n = ord('a')-ord('A')
        for i in str:
            if ord(i)<=ord('Z') and ord(i)>=ord('A'):
                res += chr(ord(i)+n)
            else:
                res += i
        return res