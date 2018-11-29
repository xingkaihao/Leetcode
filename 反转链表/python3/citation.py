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
        思路：定义三个空节点，temp1为当前节点，
        temp0为前一个节点，temp2为后一个节点，
        先将temp1指向temp0，然后将三个空节点的
        位置依次向前推进，以此类推。
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