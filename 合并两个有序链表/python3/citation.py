# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        ˼·������һ���µ�����head����������ͷ����first��
        �Ƚ�l1��l2��ǰλ�õ�ֵ��С���ѽ�С��ֵ����head.next,
        ����head�͸�ֵ��l���´�һλ����l1��l2�г���һ��������֮��
        ����һ��ʣ���lֱ�Ӹ���head.next����l����һ��Ϊ�գ�
        ��һ��ֱ�Ӹ���head.next,����first.next��
        """
        head = ListNode(0)
        first = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next