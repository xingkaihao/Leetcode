class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        ˼·���ж�target�Ƿ���nums�У�����ڣ���index���ض�Ӧλ�ã�
        ������ڣ�����-1
        '''
        if target in nums:
            return nums.index(target)
        else:
            return -1