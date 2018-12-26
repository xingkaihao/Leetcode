class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        ˼·��nС��3��ʱ��ֱ�����ж��������n���ڵ���3ʱ����һ��ѭ��ȥ���������ǵ�ÿһ�㣬
        ������Ƕ�׵�ѭ��ȥ���ÿһ���е�Ԫ�أ�����nums1�ǵ�ǰ�㡣
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        nums = [[1],[1,1]]
        for i in range(3, numRows+1):
            nums1=[1]
            for j in range(i-2):
                nums1.append(nums[i-2][j]+nums[i-2][j+1])
            nums1.append(1)
            nums.append(nums1)
        return nums