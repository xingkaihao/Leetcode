class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        ˼·����һ���ֵ佨����������Ϊͬ��ĸ�Ĵʣ�
        ��ֵΪ����ĸ���б��ڷ��ؽ���е�λ��index��
        ����strs���Ȱ�Ԫ������ת����Ԫ�飬
        �����Ԫ��û���ֵ�dic�У������Ԫ�����б�
        ����ʽ����result����Ԫ�����ֵ������Ӧ
        �ļ�ֵΪ��Ԫ����result�е�index�������Ԫ����
        �ֵ��У��Ѹ�Ԫ�ؼ��뵽result�ж�Ӧ���б��У�
        ����result��
        """
        flag = 0
        dic = {}
        result = []
        for i in strs:
            j = tuple(sorted(i))
            if j not in dic:
                dic[j]=flag
                flag+=1
                result.append([i])
            else:
                result[dic[j]].append(i)
        return result