class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ˼·����nums���򣬷���nums�м�λ�õ�����
        """
        nums.sort()
        return nums[len(nums)/2]