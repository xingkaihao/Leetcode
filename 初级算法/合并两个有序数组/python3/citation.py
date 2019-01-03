class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        思路：方法很tricky，可能是因为LeetCode的验证法，python的很多tricky操作都用不了，
        需要手动分配nums1的空间，更加坑的是，测试用例中还会在列表中多加几个0。
        思路很简单，就是把nums2中的有效元素接到nums1的有效元素的后面，然后用sort()这个
        列表函数进行排序。
        """
        nums1[m:m+n] = nums2[:n]
        nums1.sort()