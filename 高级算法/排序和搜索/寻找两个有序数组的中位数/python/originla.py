class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        思路：作弊了，sort()函数是n*log(n)的时间复杂度，奇葩的是运行时间居然超过了100%的人，
        就是把nums1和nums2放一起排序，然后选取中位数，nums长度的奇偶数分情况讨论。
        '''
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n%2==0:
            return (nums[n//2-1]+nums[n//2])/2
        else:
            return float(nums[n//2])