class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        思路：把数组遍历一遍，把target的所有元素位置存在temp中，
        返回temp的首尾元素，如果temp为空，返回[-1，-1]。
        """
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i] == target:
                temp.append(i)
        if temp==[]:
            return [-1, -1]
        else:
            return [temp[0], temp[-1]]