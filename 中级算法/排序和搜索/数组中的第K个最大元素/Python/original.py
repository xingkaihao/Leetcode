class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        ˼·��nums���򣬷��ض�Ӧλ�õ�ֵ
        '''
        nums.sort()
        return nums[-k]