class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        ˼·������������ֱ�Ӱ��б���ÿ��ƽ����֮������
        '''
        return sorted([i*i for i in A])