class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        ˼·����Ϊ����Ԫ����ֵ��ͬ������nums�����ֵһ���Ƿ�ֵ��
        '''
        return nums.index(max(nums))