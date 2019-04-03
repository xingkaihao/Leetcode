class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        思路：循环三次，第一次把i元素之前的元素乘积求出来，存起来，
        第二次循环把i元素后面的元素乘积求出来存起来，第三次循环把
        i元素前后乘积相乘，有点傻。
        '''
        if len(nums)==0:
            return []
        m = 1
        out = [[]]
        one = 1
        for k in range(1,len(nums)):
            one = one*nums[k-1]
            out.append([one])
        output = []
        two = 1
        out[0].append(1)
        out[-1].append(1)
        for j in range(1,len(nums)):
            two = two*nums[-j]
            out[-j-1].append(two)
        for i in range(len(nums)):
            output.append(out[i][0]*out[i][1])
        return output