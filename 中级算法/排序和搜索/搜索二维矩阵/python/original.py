class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        ˼·������matrixÿһ�У���indexȥ�ж���һ���Ƿ���target��
        ����У�����True�����û�м�����������֮��û���ҵ�target��
        �ͷ���False��
        """
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False