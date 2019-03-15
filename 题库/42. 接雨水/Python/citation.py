class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        思路：先找到最高的柱子，然后以最高的柱子分成两段遍历，
        第一段从前往后遍历，第二段从后往前遍历，在每段中遍历的时候，
        寻找一个较高的柱子，这个柱子只要比之前的柱子只要比之前的柱子高就可以，
        接雨量按照一个位置一个位置的计算，用较高的柱子减去当前的柱子，
        差值就是该位置的接雨量，每个位置的接雨量相加即可。
        '''
        if len(height)<3 or max(height)==0:
            return 0
        maxindex=0
        area=0
        movepeak=0
        maxindex = height.index(max(height))
        for i in range(0,maxindex):
            if movepeak<height[i]:
                movepeak=height[i]
            else:
                area+=movepeak-height[i]
        movepeak=0
        for i in range(len(height)-1,maxindex,-1):
            if movepeak<height[i]:
                movepeak=height[i]
            else:
                area+=movepeak-height[i]
        return area