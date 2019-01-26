class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        #位操作
        no_carry_sum=a^b#a与b不进位时的和，恰好与异或性质一样
        carry=(a&b)<<1#a与b的和的进位，恰好是与操作再左移一位
        return sum([no_carry_sum,carry])#前两者之和