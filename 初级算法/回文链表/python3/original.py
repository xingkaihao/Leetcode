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
        思路：i计算链表中节点数量，dic存放链表的节点序号
        和节点数值，然后遍历
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