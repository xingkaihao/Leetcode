class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        ˼·���������õ�����˼�롣������ֻ��һ������ʱ�����ؿռ���
        �����ֱ������¼�һ������ʱ����ԭ�ȵ������Ӽ������µ����֣�
        ���ǰ��������ֵ��Ӽ�������֮ǰ�����������ֵ��Ӽ���
        �������Ӽ�ֱ����Ӿ����µ������Ӽ���һ���ص����鳤�Ȳ������ӣ�
        ���ǲ�����ԭ���Ӽ��ϵ����µļ��ϼ��ɡ�
        '''
        output = [[]]
        for i in range(len(nums)):
            for j in range(len(output)):
                output.append(output[j]+[nums[i]])
        return output