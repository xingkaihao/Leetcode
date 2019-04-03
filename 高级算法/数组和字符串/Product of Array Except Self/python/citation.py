class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        思路：循环2次，第一次把i元素之前的元素乘积求出来，存起来，
        第二次循环把i元素后面的元素逐个跟求出来的乘积相乘。
        '''
        res=[0]*len(nums)
        res[0]=1
        p=1
        for i in range(1,len(nums)):
            p=p*nums[i-1]
            res[i]=p
        p=1
        for j in range(len(nums)-2,-1,-1):
            p=p*nums[j+1]
            res[j]*=p
        return res