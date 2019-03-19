class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        思路：用一个数组去保存所有不重复的元素，用另一个数组的对应位置去
        保存该元素的个数，然找到个数最多的元素，放到res中，并在原来的两
        个数组中把该元素的所有信息删除，依次类推重复k次，就能找到频率前k
        高的元素。
        '''
        name = []
        number = []
        for i in nums:
            if i in name:
                number[name.index(i)] += 1
            else:
                name.append(i)
                number.append(1)
        res = []
        for j in range(k):
            n = number.index(max(number))
            number.remove(number[n])
            res.append(name[n])
            name.remove(name[n])
        return res