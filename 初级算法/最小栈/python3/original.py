class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        思路：新建一个空数组用来做栈
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        思路：在栈的末尾加入x，需要return
        """
        return self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        思路：删除栈末尾元素，需要return
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        思路：返回栈定元素
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        思路：返回栈最小值
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()