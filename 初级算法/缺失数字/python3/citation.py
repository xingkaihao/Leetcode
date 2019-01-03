class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：求nums的元素加和，并求从0到n的加和，比较两者差值，就是缺少的那个数字
        """
        n = len(nums)
        return n*(n+1)//2-sum(nums)