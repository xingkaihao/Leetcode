class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：排序nums，遍历nums，判断是否nums[i]==i，如果不等，返回i
        否则返回len(nums)
        """
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i]!=i:
                return i
        return n