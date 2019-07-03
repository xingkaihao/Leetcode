class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        '''
        利用字典存放每种元素的每个元素对应位置，键为元素的值，键值为一个列表，
        列表中存放的是该元素在nums中的每个位置索引，最后通过在寻找列表长度的最
        大值来得到结果，如果列表长度最大值有相同的情况，取列表首尾元素差值最小的。
        '''
        dic={}
        count=0
        n=len(nums)
        res=n
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]]=[i]
            else:
                dic[nums[i]].append(i)
        for key in dic:
            m=len(dic[key])
            if m>count:
                count=m
                res=dic[key][m-1]-dic[key][0]+1
            if m==count:
                res=min(res,dic[key][m-1]-dic[key][0]+1)
        return res