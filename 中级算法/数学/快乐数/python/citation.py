class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        根据题干对快乐数的定义，我们很容易想到用循环结构来判断是否为快乐数。但是如果给定的是非快乐数，
        循环终止的条件在哪里呢？这就需要我们了解快乐数的循环结构。 
        -对于快乐数，如19，会有如下的循环过程：19->82->68->100->1 
        -对于非快乐数，如61，会有如下的循环过程：61->37->58->89->145->42->20->4->16->37 
        非快乐数最后会进入序列 4->16->37->58->89->145->42->20 的死循环

        """
        if n is None:
            return False
        tmp = 0
        while tmp != 1 and tmp != 4:
            tmp = 0
            n = str(n)
            for i in n:
                tmp += int(i) ** 2
            if tmp == 1:
                return True
            n = tmp
        if tmp == 1:
            return True
        return False