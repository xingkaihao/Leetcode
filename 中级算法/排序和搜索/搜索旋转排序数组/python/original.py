class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        ˼·����index�����ҵ����������û��target�����쳣��ⷵ��-1
        '''
        try:
            return nums.index(target)
        except:
            return -1