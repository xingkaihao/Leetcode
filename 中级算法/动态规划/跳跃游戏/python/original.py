class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        思路：因为有0才不能调到最后，所以把0的位置都保存起来，
        在0之前找到能跳过0的元素，如果找不到，就是false，
        如果每个0都能跳过，就是true。'''
        if len(nums)<=1:
            return True
        zero = []
        i = -1
        while True:
            if 0 in nums[i+1:]:
                n = nums[i+1:].index(0)+i+1
                zero.append(n)
                i = n
            else:
                break
        point = 0
        while point < len(zero):
            l = len(zero)
            for k in range(zero[point]-1,-1,-1):
                if nums[k]+k >= len(nums)-1:
                    zero = zero[:point]
                    break
                if zero[point]-k < nums[k]:
                    zero.remove(zero[point])
                    break
            if len(zero) == l:
                return False
        if len(zero)==0:
            return True
        else:
            return False