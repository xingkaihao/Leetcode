class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        思路：动态规划思想，把复杂问题分解成简单子问题，每个amount对应的答案，
        都是一个小于amount的amount1答案加1: amount1<amount, amounut1+coin[i]==amount,
        依次类推，生成一个从1到amount的字典，这样就可以得到amount对应的答案了。
        '''
        coins.sort() #给硬币从小到大排序
        dp = {0:0} #生成字典dp，并且当总金额为0时，最少硬币个数为0
        for i in range(1,amount + 1):
            dp[i] = amount + 1 #因为硬币个数不可能大于amount，所以赋值amount + 1便于比较
            for j in coins:
                if j <= i:
                    dp[i]=min(dp[i],dp[i-j]+1)
                else:
                    break
        if dp[amount] == amount + 1: #当最小硬币个数为初始值时，代表不存在硬币组合能构成此金额
            return -1
        else:
            return dp[amount]