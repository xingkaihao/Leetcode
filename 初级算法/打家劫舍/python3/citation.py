class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ˼·��ͨ��last��nowȥ�����ۼӺͣ��������ĺ͸���now��
        ��Ϊ��last+i�����Ի�������ڣ�ͨ��max()ȥѡ������ʵ�
        �Ӻ�Ԫ�ء�
        """
        now = 0
        last = 0
        for i in nums:
            last, now = now, max(last+i, now)
        return now