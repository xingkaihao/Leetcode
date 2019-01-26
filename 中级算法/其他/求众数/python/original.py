class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：先判断nums是否是单元素，如果是，直接返回该元素，
        如果不是，建立一个字典，通过遍历nums的方式去让字典记录
        nums的情况，键为元素，键值为元素个数，当元素个数大于n/2
        就返回该元素。
        """
        n = len(nums)
        if n==1 :
            return nums[0]
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
                if dic[i]>n//2:
                    return i