
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        思路：使用Counter计数器
        '''
        from collections import Counter
        c = Counter(nums)
        return [i[0] for i in c.most_common(k)]