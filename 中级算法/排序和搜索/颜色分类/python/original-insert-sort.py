class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        ˼·��ʹ�ò�������ɨ������numsһ�飬���ΰ�δɨ��ĵ�Ԫ����
        ��С��Ԫ�غ͵�ǰԪ�ؽ�����
        """
        red = 0
        white = 1
        blue = 2
        for i in range(len(nums)):
            m = nums[i:].index(min(nums[i:]))
            nums[i],nums[m+i] = nums[m+i],nums[i]