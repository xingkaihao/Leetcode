class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ˼·����nums��Ԫ�ؼӺͣ������0��n�ļӺͣ��Ƚ����߲�ֵ������ȱ�ٵ��Ǹ�����
        """
        n = len(nums)
        return n*(n+1)//2-sum(nums)