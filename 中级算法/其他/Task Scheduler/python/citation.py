class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        ˼·����outputȥ��¼ÿ������ĸ�������һ��ѭ��ȥ���������̣�
        ֮����һ��ѭ��ȥ�ҳ��ж��ٸ�����ظ�������������ͳ�������и�
        ��������ֵĴ��������Ȱ��Ŵ����������񡣴���������������
        ��֮�������ʱ����Ϊ��max(����)-1��*��n+1��+1����������ֱ��
        ��ռ��ɡ��ֳ��������������len(tasks)��(max_o-1)*(n+1)+count
        �Ľϴ�ֵ��
        """
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] = output[ord(i)-ord('A')]+1
 
        count = 0
        len_o = 0
        max_o = max(output)
        for i in output:
            if i==max_o:
                count = count+1
                    
        return max(len(tasks),(max_o-1)*(n+1)+count) 