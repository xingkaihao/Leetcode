class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        ˼·�����������һ�飬��target������Ԫ��λ�ô���temp�У�
        ����temp����βԪ�أ����tempΪ�գ�����[-1��-1]��
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