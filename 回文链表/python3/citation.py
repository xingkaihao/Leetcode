# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        ˼·���������нڵ�ֵ��˳������temp�б��У�
        ֮����֤temp�ǲ��ǻ����б�
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        return temp == temp[::-1]