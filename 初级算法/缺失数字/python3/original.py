class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ˼·������nums������nums���ж��Ƿ�nums[i]==i��������ȣ�����i
        ���򷵻�len(nums)
        """
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i]!=i:
                return i
        return n