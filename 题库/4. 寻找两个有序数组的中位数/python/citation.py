class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        ˼·������������ƴ��������֮�����������
        �������������͵���len(nums)//2λ�õ���ȡƽ�������ɡ�
        '''
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)//2
        return (nums[n]+nums[~n])/2 # ~n=-n-1