# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        temp = ListNode(self.reverseList(head.next))
        head.next.next = head
        head.next = None
        return temp.val
