class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        思路：从后往前遍历nums，寻找能调到最后位置的元素，找到该元素之后，
        再寻找能调到该位置的元素，如果最后能回到起始位置，就说明能完成，否则
        就是完不成任务。'''
        i = len(nums) - 1
        for j in range(len(nums)-2, -1, -1):
            if i - j <= nums[j]:
                i = j
        return i == 0