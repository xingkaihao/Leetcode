class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        ˼·����������prices��Ѱ���Ѿ��������������е���Сֵmin_price��
        ������������ǰԪ�غ�min_price�Ĳ�ֵ������max_profile���бȽϣ�
        �ѽϴ�ֵ����max_profile������max_profile
        """
        if len(prices)<2:
            return 0
        min_price = prices[0]
        max_profile = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profile = max(max_profile, i - min_price)
        return max_profile