class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        思路：遍历从nums的第二个元素到倒数第二个元素，判断如果当前
        元素大于之前元素的最小值，并且小于后面元素的最大值，则返回
        True,遍历完之后返回False。
        """
        for i in range(1, len(nums)-1):
            if min(nums[:i]) < nums[i] < max(nums[i+1:]):
                return True
        return False