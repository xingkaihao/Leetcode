class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        ˼·�����ҵ���ߵ����ӣ�Ȼ������ߵ����ӷֳ����α�����
        ��һ�δ�ǰ����������ڶ��δӺ���ǰ��������ÿ���б�����ʱ��
        Ѱ��һ���ϸߵ����ӣ��������ֻҪ��֮ǰ������ֻҪ��֮ǰ�����Ӹ߾Ϳ��ԣ�
        ����������һ��λ��һ��λ�õļ��㣬�ýϸߵ����Ӽ�ȥ��ǰ�����ӣ�
        ��ֵ���Ǹ�λ�õĽ�������ÿ��λ�õĽ�������Ӽ��ɡ�
        '''
        if len(height)<3 or max(height)==0:
            return 0
        maxindex=0
        area=0
        movepeak=0
        maxindex = height.index(max(height))
        for i in range(0,maxindex):
            if movepeak<height[i]:
                movepeak=height[i]
            else:
                area+=movepeak-height[i]
        movepeak=0
        for i in range(len(height)-1,maxindex,-1):
            if movepeak<height[i]:
                movepeak=height[i]
            else:
                area+=movepeak-height[i]
        return area