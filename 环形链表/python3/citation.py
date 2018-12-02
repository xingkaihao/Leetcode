# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        ˼·������ָ�룬һ��һ����fast��slow�ƶ��ٶȵ�������
        ��ѭ���������ȴ�����ʱ����ָ��������
        ע�⣺while�е��ж�����fast and fast.next˳���ܷ���
        ����ᱨ��
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False