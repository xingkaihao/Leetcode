# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        ������ָ�룬һ��ָ��p��ǰ����ɨ����������һ��ָ��q��ָ��p�Ĳ���Ϊn+1��
        ��ô��pָ��β����Nullʱ��ָ��qǡ��ָ��Ҫɾ���ڵ��ǰһ���ڵ㡣
        ���ڿ���ɾ��ͷ���ڵ㣬αװһ���µ�ͷ�����������
        """
        new_head = ListNode(0)
        new_head.next = head
        fast = slow = new_head
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return new_head.next