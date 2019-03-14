class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        思路：把两个数组拼接起来，之后把数组排序，
        判断数组的数量奇偶，如果为奇数，返回中间的
        数就可以，如果为偶数，返回中间两个数的平均数。
        '''
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            return (nums[n//2]+nums[n//2-1])/2
        else:
            return nums[n//2]