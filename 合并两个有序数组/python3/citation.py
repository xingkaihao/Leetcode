class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        ˼·��������tricky����������ΪLeetCode����֤����python�ĺܶ�tricky�������ò��ˣ�
        ��Ҫ�ֶ�����nums1�Ŀռ䣬���ӿӵ��ǣ����������л������б��ж�Ӽ���0��
        ˼·�ܼ򵥣����ǰ�nums2�е���ЧԪ�ؽӵ�nums1����ЧԪ�صĺ��棬Ȼ����sort()���
        �б�����������
        """
        nums1[m:m+n] = nums2[:n]
        nums1.sort()