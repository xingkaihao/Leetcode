class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        思路：用output去记录每种任务的个数，用一个循环去完成这个过程，
        之后用一个循环去找出有多少个最大重复数量的任务；先统计数组中各
        个任务出现的次数。优先安排次数最多的任务。次数最多的任务安排完
        成之后所需的时间间隔为（max(次数)-1）*（n+1）+1。其余任务直接
        插空即可。分成两种情况，返回len(tasks)和(max_o-1)*(n+1)+count
        的较大值。
        """
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] = output[ord(i)-ord('A')]+1
 
        count = 0
        len_o = 0
        max_o = max(output)
        for i in output:
            if i==max_o:
                count = count+1
                    
        return max(len(tasks),(max_o-1)*(n+1)+count) 