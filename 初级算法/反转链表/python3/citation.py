# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        ˼·�����������սڵ㣬temp1Ϊ��ǰ�ڵ㣬
        temp0Ϊǰһ���ڵ㣬temp2Ϊ��һ���ڵ㣬
        �Ƚ�temp1ָ��temp0��Ȼ�������սڵ��
        λ��������ǰ�ƽ����Դ����ơ�
        """
        if head == None:
            return head
        temp0 = None
        temp1 = head
        temp2 = head.next
        while temp2:
            temp1.next = temp0
            temp0 =temp1
            temp1 = temp2
            temp2 = temp2.next
        temp1.next = temp0
        head = temp1
        return head