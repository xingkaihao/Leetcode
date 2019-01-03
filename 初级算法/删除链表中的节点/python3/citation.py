# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        把下一个节点的值赋给要删除的节点，把下个节点的next地址赋给要删除的替换要
        删除的节点next。
        """
        node.val = node.next.val
        node.next = node.next.next