class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ˼·�����ж�nums�Ƿ��ǵ�Ԫ�أ�����ǣ�ֱ�ӷ��ظ�Ԫ�أ�
        ������ǣ�����һ���ֵ䣬ͨ������nums�ķ�ʽȥ���ֵ��¼
        nums���������ΪԪ�أ���ֵΪԪ�ظ�������Ԫ�ظ�������n/2
        �ͷ��ظ�Ԫ�ء�
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