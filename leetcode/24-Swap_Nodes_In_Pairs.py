# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        temp = head
        
        while temp and temp.next:
            val = temp.val
            temp.val = temp.next.val
            temp.next.val = val
            temp = temp.next.next
        return head