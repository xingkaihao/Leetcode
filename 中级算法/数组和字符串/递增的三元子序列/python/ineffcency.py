class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        ˼·��������nums�ĵڶ���Ԫ�ص������ڶ���Ԫ�أ��ж������ǰ
        Ԫ�ش���֮ǰԪ�ص���Сֵ������С�ں���Ԫ�ص����ֵ���򷵻�
        True,������֮�󷵻�False��
        """
        for i in range(1, len(nums)-1):
            if min(nums[:i]) < nums[i] < max(nums[i+1:]):
                return True
        return False