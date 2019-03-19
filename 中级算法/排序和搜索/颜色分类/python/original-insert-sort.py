class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        思路：使用插入排序，扫描整个nums一遍，依次把未扫描的的元素中
        最小的元素和当前元素交换。
        """
        red = 0
        white = 1
        blue = 2
        for i in range(len(nums)):
            m = nums[i:].index(min(nums[i:]))
            nums[i],nums[m+i] = nums[m+i],nums[i]