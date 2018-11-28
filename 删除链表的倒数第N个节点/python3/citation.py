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
        用两个指针，一个指针p从前到后扫描整个链表，一个指针q慢指针p的步数为n+1，
        那么当p指向尾部的Null时，指针q恰好指向要删除节点的前一个节点。
        由于可能删除头部节点，伪装一个新的头部方便操作。
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