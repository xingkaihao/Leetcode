class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        ˼·���Ӻ���ǰ����nums��Ѱ���ܵ������λ�õ�Ԫ�أ��ҵ���Ԫ��֮��
        ��Ѱ���ܵ�����λ�õ�Ԫ�أ��������ܻص���ʼλ�ã���˵������ɣ�����
        �����겻������'''
        i = len(nums) - 1
        for j in range(len(nums)-2, -1, -1):
            if i - j <= nums[j]:
                i = j
        return i == 0