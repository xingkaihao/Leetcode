class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        ˼·��ѭ�����Σ���һ�ΰ�iԪ��֮ǰ��Ԫ�س˻����������������
        �ڶ���ѭ����iԪ�غ����Ԫ�س˻��������������������ѭ����
        iԪ��ǰ��˻���ˣ��е�ɵ��
        '''
        if len(nums)==0:
            return []
        m = 1
        out = [[]]
        one = 1
        for k in range(1,len(nums)):
            one = one*nums[k-1]
            out.append([one])
        output = []
        two = 1
        out[0].append(1)
        out[-1].append(1)
        for j in range(1,len(nums)):
            two = two*nums[-j]
            out[-j-1].append(two)
        for i in range(len(nums)):
            output.append(out[i][0]*out[i][1])
        return output