class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ˼·�������������飬����������ɾ��
        """
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i+=1
                
        return len(nums)