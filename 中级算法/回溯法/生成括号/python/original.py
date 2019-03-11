class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        ˼·��n�����ŵ����������n-1��������ÿ������¶����һ�����ŵ����ģ�
        ��˴�1�����ſ�ʼ�𲽼����ţ�ֱ���õ�n�����ŵ����������Ҫ�õ�����
        һ�����ŵ����������������ÿ��λ�ü������ŵ��������������û�г��ֹ���
        �ͱ���������������ֹ���������
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