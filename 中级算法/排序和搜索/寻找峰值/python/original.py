class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        思路：因为相邻元素数值不同，所以nums的最大值一定是峰值。
        '''
        return nums.index(max(nums))