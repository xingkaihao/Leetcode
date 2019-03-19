class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        ˼·����������ָ��ֱ�ָ��0��2��0��ָ���Ǵ�ǰ�����ƶ���
        2��ָ���ǴӺ���ǰ�ƶ���ɨ������nums����ǰԪ��Ϊ1ʱ��
        ��ִ�в�����ֱ����һ������ǰԪ��Ϊ2ʱ����ǰԪ����2ָ��
        Ԫ�ؽ��������ҵ�ǰָ�벻�ƶ�����ǰԪ��Ϊ0ʱ����ǰԪ�غ�
        0ָ��Ԫ�ؽ�������ǰָ��������һλ����Ϊ0Ԫ��ָ���λ��Ԫ��
        �Ѿ���ɨ������������ơ�
        """
        zero, two = -1, len(nums)
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]
            else:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1