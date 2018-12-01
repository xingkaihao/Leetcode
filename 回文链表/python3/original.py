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
        ˼·��i���������нڵ�������dic�������Ľڵ����
        �ͽڵ���ֵ��Ȼ�����
        """
        i = 0
        dic = {}
        while head:
            i += 1
            dic[i] = head.val
            head = head.next
        for j in range(1, int(i/2)+1):
            if dic[j] != dic[i-j+1]:
                return False
        return True