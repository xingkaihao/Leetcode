class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        ˼·��ѭ��2�Σ���һ�ΰ�iԪ��֮ǰ��Ԫ�س˻����������������
        �ڶ���ѭ����iԪ�غ����Ԫ�������������ĳ˻���ˡ�
        '''
        res=[0]*len(nums)
        res[0]=1
        p=1
        for i in range(1,len(nums)):
            p=p*nums[i-1]
            res[i]=p
        p=1
        for j in range(len(nums)-2,-1,-1):
            p=p*nums[j+1]
            res[j]*=p
        return res