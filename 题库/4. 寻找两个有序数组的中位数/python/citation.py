class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        思路：把两个数组拼接起来，之后把数组排序，
        把数组中正数和倒数len(nums)//2位置的数取平均数即可。
        '''
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)//2
        return (nums[n]+nums[~n])/2 # ~n=-n-1