class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：通过last和now去计算累加和，保留最大的和赋给now，
        因为是last+i，所以会避免相邻，通过max()去选择最合适的
        加和元素。
        """
        now = 0
        last = 0
        for i in nums:
            last, now = now, max(last+i, now)
        return now