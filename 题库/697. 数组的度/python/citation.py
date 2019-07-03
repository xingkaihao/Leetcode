class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        '''
        �����ֵ���ÿ��Ԫ�ص�ÿ��Ԫ�ض�Ӧλ�ã���ΪԪ�ص�ֵ����ֵΪһ���б�
        �б��д�ŵ��Ǹ�Ԫ����nums�е�ÿ��λ�����������ͨ����Ѱ���б��ȵ���
        ��ֵ���õ����������б������ֵ����ͬ�������ȡ�б���βԪ�ز�ֵ��С�ġ�
        '''
        dic={}
        count=0
        n=len(nums)
        res=n
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]]=[i]
            else:
                dic[nums[i]].append(i)
        for key in dic:
            m=len(dic[key])
            if m>count:
                count=m
                res=dic[key][m-1]-dic[key][0]+1
            if m==count:
                res=min(res,dic[key][m-1]-dic[key][0]+1)
        return res