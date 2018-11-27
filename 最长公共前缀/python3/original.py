class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        ˼·����strs�ĵ�һ���ַ�������Ϊ�Ƚ��ַ�temp��
        ȥ�ֱ��strs�е�ÿ���ַ����Ƚϣ������ַ����ȽϹ����У�
        �Խ϶̵��ַ���Ϊ��׼���ֱ�Ƚ��ַ����е�ÿ���ַ��Ƿ�һ�£�
        ������ֲ�һ�£��Ͱ�temp�дӲ�һ�µ��ַ���ʼ��
        ɾ�����������ַ�����������ѭ����
        ��������ַ��Ƚϵ�ѭ�������˻�û�г��ֲ�һ�£�
        �Ͱ�temp�ĳ���ȡ�ɸ�ѭ���ĳ��ȡ�
        """
        if not len(strs):
            return ""
        temp = strs[0]
        for i in strs:
            if not len(i):
                return ""
            for j in range(min(len(i),len(temp))):
                if temp[j] != i[j]:
                    temp = temp[:j]
                    break
                if j+1 == min(len(i),len(temp)):
                    temp = temp[:j+1]
        return temp