class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        ˼·��������������ĸ��Ӧ���ֵ䣬����digits�еĵ�һ�����ֺ͵ڶ������ֱ����õ�
        ��ĸ��Ͻ�����øý���ٺ͵��������ֱ����õ���ĸ��Ͻ�����Դ����ơ�
        '''
        if not digits:
            return []
        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = [i for i in digit2chars[digits[0]]]
        for j in digits[1:]:
            res = [k+j for j in digit2chars[j] for k in res]
        return res