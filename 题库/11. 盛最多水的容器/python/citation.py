class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        ˼·�� �ƽ��� 
        ÿ���������˶���ȥ�̵���һ�� 
        ��ѡ��̵���һ�ˡ�S=С�ڵ��ڴ˶˵ĸ�*С�ڵ��ڵ�ǰ��������䳤�ȡ�
        ��������Ҳ��ѡ���������ҵ�һ�����Σ���˲����ٿ��Ƕ̵�һ�ˣ�ֱ����ȥ�ƽ�
        '''
        first = 0
        last = len(height)-1
        res = 0
        while last>first:
            res = max((last - first)*min(height[first],height[last]),res)
            if height[last]<height[first]:
                last-=1
            elif height[first]<height[last]:
                first += 1
            else:
                last -= 1
        return res