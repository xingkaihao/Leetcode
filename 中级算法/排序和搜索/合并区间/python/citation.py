# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        '''
        思路：先根据intervals.start排序，之后去遍历每个intervals，
        如果相邻的intervals有的重叠，就合并，否则就直接加入re。
        '''
        if len(intervals)<2:
            return intervals
        intervals = sorted(intervals, key=lambda startone: startone.start)
        re = []
        for i in range(1, len(intervals)):
            last = intervals[i-1]
            now = intervals[i]
            if now.start<=last.end:
                now.end = max(intervals[i].end, last.end)
                now.start = last.start
            else:
                re.append(intervals[i-1])
        re.append(intervals[i])
        return re