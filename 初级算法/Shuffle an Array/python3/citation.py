class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        思路：初始化函数中通过origin和output把nums和它的一个副本传递到另外两个函数中
        """
        self.origin = nums[:]
        self.output = nums
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        思路：直接返回origin
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        思路：利用random.randint，生成[i, n-1]中的一个整数，将i位置的元素和随机生成的位置元素
        位置交换
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