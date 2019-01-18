class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        ˼·�����s����С�ڵ���1��ֱ�ӷ���s�ĳ��ȣ�
        �����������s������temp���浱ǰ���ظ����ַ�����
        ����stack�������еĲ��ظ��ַ������ȣ�
        �����ǰ�ַ�����temp�У��ѵ�ǰ�ַ�����temp��
        �����temp�ĳ��ȱ�����stack�У�����temp����
        ��ǰ�ַ��ظ����ַ�����֮ǰ���ַ�ȫ��ɾ����
        �ѵ�ǰ�ַ����뵽tempĩβ������������
        ��temp�ĳ��ȼ���stack�У�����stack�����ֵ��
        """
        if len(s)<=1:
            return len(s)
        stack=[]
        temp=[s[0]]
        for i in range(1, len(s)):
            if s[i] not in temp:
                temp.append(s[i])
            else:
                stack.append(len(temp))
                k=temp.index(s[i])
                temp=temp[k+1:]
                temp.append(s[i])
        stack.append(len(temp))
        return max(stack)