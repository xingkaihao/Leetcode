class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        思路：遍历matrix每一行，用index去判断这一行是否有target，
        如果有，返回True，如果没有继续，遍历完之后还没有找到target，
        就返回False。
        """
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False