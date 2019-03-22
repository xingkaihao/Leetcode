class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        思路：判断target是否在nums中，如果在，用index返回对应位置，
        如果不在，返回-1
        '''
        if target in nums:
            return nums.index(target)
        else:
            return -1