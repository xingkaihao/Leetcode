class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思路：遍历整个prices，寻找已经遍历过的数组中的最小值min_price，
        遍历过程中求当前元素和min_price的差值，并跟max_profile进行比较，
        把较大值赋给max_profile，返回max_profile
        """
        if len(prices)<2:
            return 0
        min_price = prices[0]
        max_profile = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profile = max(max_profile, i - min_price)
        return max_profile