# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = []
        while(head != None):
            temp = head.val
            queue.append(temp)
            head = head.next

        # res = int("".join(map(str, queue)))
        if len(queue) > 1:
            res = 0
            for i, d in enumerate(queue[::-1]):
                if d < 0:
                    d = d * -1
                d = d * 1
                res += d * 10**i
            rev = 0
            while res > 0:
                rev = rev * 10 + res % 10
                res = res / 10
            if res == rev:
                return True
            return False
        return True
