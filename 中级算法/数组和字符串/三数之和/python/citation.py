class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        ˼·��res������Ž����minus�������nums�еĸ�����plus�������nums�еķǸ�����
        һ��forѭ����������minus��plus���������ֵ䣬�ֵ�ļ�Ϊnums�е�Ԫ�أ���ֵΪ��Ԫ��
        ��nums�е�������minus��plus����set()�������ֱ�ֵ��m��p����һ��if�ж��Ƿ������
        [0,0,0]�������������Ƕ�׵�forѭ������m��p��temp��ʾ��������Ҫ�����֣�������������ֵ��У�
        �������������������
        ���temp��i��j�е�һ�������Ԫ����nums�е�����Ҫ����1������temp<i����temp>j
        �����Ϊ�˱�����ָ�����
        ����������nums��ӵ�res�У�����res��
        """
        res, minus, plus, count = [], [], [], {}
        for num in nums:
            count[num] = count.get(num, 0)+1
            if num < 0:
                minus.append(num)
            else:
                plus.append(num)
        m, p = set(minus), set(plus)
        if 0 in count and count[0] >= 3:
            res.append([0, 0, 0])
        for i in m:
            for j in p:
                temp = -i - j
                if temp in count and (temp < i or temp > j or (temp in {i, j} and count[temp] > 1)):
                    res.append([i, j, temp])
        return res
