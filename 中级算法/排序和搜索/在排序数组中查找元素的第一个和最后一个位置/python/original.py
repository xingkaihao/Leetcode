class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        思路：先检测是否target是否在nums中，
        如果在nums中，就用index函数得到target
        索引，之后再把nums反过来，再得到target索引，
        这样就得到target的第一个和最后一个位置了。
        """
        if target not in nums:
            return [-1,-1]
        res = []
        res.append(nums.index(target))
        num = nums[::-1]
        n = num.index(target)
        res.append(len(nums)-n-1)
        return res