class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        ˼·������������ȫ��������һ����ȫ�����ҵ�0��λ�ã��������λ�õ��кź��кţ�
        ���������ü���ȥ����ģ�����ȥ�أ�����֮��Ѽ���ת��Ϊ�б�����ʹ�á��ڶ���
        �����ǰ�Ҫ���λ����0���ѱ�����к�������0��������кű�����0��
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