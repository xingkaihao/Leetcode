class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：把nums排序，返回nums中间位置的数。
        """
        nums.sort()
        return nums[len(nums)/2]