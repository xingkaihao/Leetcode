class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        ˼·���ȼ���Ƿ�target�Ƿ���nums�У�
        �����nums�У�����index�����õ�target
        ������֮���ٰ�nums���������ٵõ�target������
        �����͵õ�target�ĵ�һ�������һ��λ���ˡ�
        """
        if target not in nums:
            return [-1,-1]
        res = []
        res.append(nums.index(target))
        num = nums[::-1]
        n = num.index(target)
        res.append(len(nums)-n-1)
        return res