class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        ˼·����һ������ȥ�������в��ظ���Ԫ�أ�����һ������Ķ�Ӧλ��ȥ
        �����Ԫ�صĸ�����Ȼ�ҵ���������Ԫ�أ��ŵ�res�У�����ԭ������
        �������аѸ�Ԫ�ص�������Ϣɾ�������������ظ�k�Σ������ҵ�Ƶ��ǰk
        �ߵ�Ԫ�ء�
        '''
        name = []
        number = []
        for i in nums:
            if i in name:
                number[name.index(i)] += 1
            else:
                name.append(i)
                number.append(1)
        res = []
        for j in range(k):
            n = number.index(max(number))
            number.remove(number[n])
            res.append(name[n])
            name.remove(name[n])
        return res