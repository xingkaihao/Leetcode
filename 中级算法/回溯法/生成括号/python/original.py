class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        思路：n个括号的所有情况是n-1个括号在每种情况下多加入一个括号得来的，
        因此从1个括号开始逐步加括号，直到得到n个括号的所有情况，要得到加入
        一个括号的所有情况，遍历在每个位置加入括号的情况，如果该情况没有出现过，
        就保留下来，如果出现过，就舍弃
        '''
        res = ["()"]
        for i in range(1,n):
            temp = []
            for j in res:
                for k in range(len(j)):
                    tem = j[:k]+"()"+j[k:]
                    if tem not in temp:
                        temp.append(tem)
            res = temp
        return res