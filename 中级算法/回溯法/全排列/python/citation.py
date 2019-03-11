class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        ˼·��ͨ���ݹ�ķ�ʽ��ɣ���ȷ����һ��λ�õ����֣�
        Ȼ��ʣ��λ�����У���һ��λ�õ�����Ҫ����nums������
        ���֡�
        '''
        res = []
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, nums[::-1]]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i+1:]
            for item in self.permute(newnums):
                res.append([num] + item)
        return res