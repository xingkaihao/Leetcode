class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        思路：进行两次完全遍历，第一次完全遍历找到0的位置，并保存该位置的行号和列号，
        本方法是用集合去保存的，可以去重，遍历之后把集合转换为列表，方便使用。第二次
        遍历是把要求的位置置0，把保存的行号整行置0，保存的列号遍历置0。
        """
        row = len(matrix)
        column = len(matrix[0])
        row1 = set()
        column1 = set()
        for i in range(row):
            for l in range(column):
                if matrix[i][l]==0:
                    row1.add(i)
                    column1.add(l)
        row1 = list(row1)
        column1 = list(column1)
        for j in range(row):
            if j in row1:
                matrix[j]=[0]*column
            else :
                for k in column1:
                    matrix[j][k]=0