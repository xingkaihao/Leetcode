class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        思路：用index函数找到索引，如果没有target，用异常检测返回-1
        '''
        try:
            return nums.index(target)
        except:
            return -1