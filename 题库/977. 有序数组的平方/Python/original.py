class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        思路：暴力方法，直接把列表中每项平方，之后排序。
        '''
        return sorted([i*i for i in A])