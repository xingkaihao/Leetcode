class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        ˼·�������ˣ�sort()������n*log(n)��ʱ�临�Ӷȣ������������ʱ���Ȼ������100%���ˣ�
        ���ǰ�nums1��nums2��һ������Ȼ��ѡȡ��λ����nums���ȵ���ż����������ۡ�
        '''
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n%2==0:
            return (nums[n//2-1]+nums[n//2])/2
        else:
            return float(nums[n//2])