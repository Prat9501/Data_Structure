# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        first = second = temp

        for i in range(n):
            first = first.next

        while first.next is not None:
            first = first.next
            second = second.next
        else:
            second.next = second.next.next

        return temp.next
