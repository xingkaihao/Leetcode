class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        ˼·����̬�滮˼�룬�Ѹ�������ֽ�ɼ������⣬ÿ��amount��Ӧ�Ĵ𰸣�
        ����һ��С��amount��amount1�𰸼�1: amount1<amount, amounut1+coin[i]==amount,
        �������ƣ�����һ����1��amount���ֵ䣬�����Ϳ��Եõ�amount��Ӧ�Ĵ��ˡ�
        '''
        coins.sort() #��Ӳ�Ҵ�С��������
        dp = {0:0} #�����ֵ�dp�����ҵ��ܽ��Ϊ0ʱ������Ӳ�Ҹ���Ϊ0
        for i in range(1,amount + 1):
            dp[i] = amount + 1 #��ΪӲ�Ҹ��������ܴ���amount�����Ը�ֵamount + 1���ڱȽ�
            for j in coins:
                if j <= i:
                    dp[i]=min(dp[i],dp[i-j]+1)
                else:
                    break
        if dp[amount] == amount + 1: #����СӲ�Ҹ���Ϊ��ʼֵʱ����������Ӳ������ܹ��ɴ˽��
            return -1
        else:
            return dp[amount]