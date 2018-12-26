class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        思路：n小于3的时候直接用判断输出，当n大于等于3时，用一个循环去添加杨辉三角的每一层，
        用里面嵌套的循环去添加每一层中的元素，其中nums1是当前层。
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