class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        ˼·����Ϊ��0�Ų��ܵ���������԰�0��λ�ö�����������
        ��0֮ǰ�ҵ�������0��Ԫ�أ�����Ҳ���������false��
        ���ÿ��0��������������true��'''
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