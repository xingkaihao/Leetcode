class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        思路： 逼近法 
        每次左右两端都舍去短的那一端 
        若选择短的那一端【S=小于等于此端的高*小于等于当前的最大区间长度】
        至多的面积也是选择最左最右的一个矩形，因此不必再考虑短的一端，直接舍去逼近
        '''
        first = 0
        last = len(height)-1
        res = 0
        while last>first:
            res = max((last - first)*min(height[first],height[last]),res)
            if height[last]<height[first]:
                last-=1
            elif height[first]<height[last]:
                first += 1
            else:
                last -= 1
        return res