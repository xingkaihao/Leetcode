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
        思路：定义一个新的链表head，并把链表头赋给first，
        比较l1和l2当前位置的值大小，把较小的值赋给head.next,
        并且head和赋值的l向下窜一位，当l1或l2中出有一个遍历完之后，
        将另一个剩余的l直接赋给head.next；当l中有一个为空，
        另一个直接赋给head.next,返回first.next。
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