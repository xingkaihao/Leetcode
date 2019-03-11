class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        思路：通过递归的方式完成，先确定第一个位置的数字，
        然后剩下位置排列，第一个位置的数字要遍历nums中所有
        数字。
        '''
        res = []
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, nums[::-1]]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i+1:]
            for item in self.permute(newnums):
                res.append([num] + item)
        return res