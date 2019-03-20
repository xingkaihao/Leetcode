class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        思路：nums排序，返回对应位置的值
        '''
        nums.sort()
        return nums[-k]