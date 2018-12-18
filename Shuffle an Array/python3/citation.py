class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        ˼·����ʼ��������ͨ��origin��output��nums������һ���������ݵ���������������
        """
        self.origin = nums[:]
        self.output = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        ˼·��ֱ�ӷ���origin
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        ˼·������random.randint������[i, n-1]�е�һ����������iλ�õ�Ԫ�غ�������ɵ�λ��Ԫ��
        λ�ý���
        """
        n = len(self.output)
        for i in range(n):
            j = random.randint(i, n-1)
            self.output[i], self.output[j] = self.output[j], self.output[i]
        return self.output


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()