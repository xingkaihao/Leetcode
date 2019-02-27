class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        ˼·�����ȱ߽��������ã����numRowsС��s���Ȼ���Ϊ1����ֱ�ӷ���s��
        s��ΪnumRows���㣬ÿ��ֱ���������еĲ�ͬλ�ã�����ĳ���ΪnumRows��
        ��ʼ��Ӧλ��Ϊ''��֮���ñ���s����s��ÿ���ַ��ŵ���Ӧ������λ���У�
        idxΪ����λ�ã�step���Ʒ������������е��ַ�����ƴ��������
        """
        if numRows>len(s) or numRows==1:
            return s
        res=['']*numRows
        idx,step=0,1
        for i in s:
            res[idx]+=i
            if idx==0:
                step=1
            elif idx==numRows-1:
                step=-1
            idx+=step
        return ''.join(res)