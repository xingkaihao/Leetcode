class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        思路：建立数字与字母对应的字典，先用digits中的第一个数字和第二个数字遍历得到
        字母组合结果，用该结果再和第三个数字遍历得到字母组合结果，以此类推。
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