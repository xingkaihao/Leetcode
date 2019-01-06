class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：遍历整个数组，遇到副本就删除
        """
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i+=1
                
        return len(nums)