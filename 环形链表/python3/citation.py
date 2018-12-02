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
        思路：两个指针，一快一慢，fast是slow移动速度的两倍，
        当循环链表环长度次数的时候，两指针相遇。
        注意：while中的判断条件fast and fast.next顺序不能反，
        否则会报错。
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False