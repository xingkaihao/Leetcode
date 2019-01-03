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
        思路：把链表中节点值按顺序存放在temp列表中，
        之后验证temp是不是回文列表。
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        return temp == temp[::-1]