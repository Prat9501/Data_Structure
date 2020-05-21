# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        temp_1 = head
        temp_2 = head.next
        while(temp_1 != temp_2):
            if temp_2 == None or temp_2.next == None:
                return False
            temp_1 = temp_1.next
            temp_2 = temp_2.next.next
        return True
