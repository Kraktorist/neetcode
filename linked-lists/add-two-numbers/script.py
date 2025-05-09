#!/usr/bin/env python

from ListNode import ListNode
from typing import Optional

# sum of two lists

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         sum = 0
#         step = 0
#         while l1 or l2:
#             if not l1:
#                 curr_sum = l2.val
#                 l2 = l2.next
#             elif not l2:
#                 curr_sum = l1.val
#                 l1 = l1.next
#             else:
#                 curr_sum = l1.val + l2.val
#                 l2 = l2.next
#                 l1 = l1.next
#             sum += curr_sum * 10 ** step
#             step += 1
#         return sum

# first succesful submission

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         """
#         """
#         tens = 0
#         head = ListNode()
#         prev = head
#         while l1 or l2 or tens:
#             if l1 and l2:
#                 sum = l1.val + l2.val
#                 l1, l2 = l1.next, l2.next
#             elif l2 and not l1:
#                 sum = l2.val
#                 l2 = l2.next
#             elif l1 and not l2:
#                 sum = l1.val
#                 l1 = l1.next
#             sum = sum + tens
#             if sum > 9:
#                 tens = 1
#                 sum = sum - 10
#             else:
#                 tens = 0
            
#             curr = ListNode(sum)
#             prev.next = curr
#             prev = curr
#             sum = 0
#         return head.next

# second succesful submission

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         """
#         """
#         sum = 0
#         head = ListNode()
#         prev = head
#         while l1 or l2 or sum:
#             if l1 and l2:
#                 sum += l1.val + l2.val
#                 l1, l2 = l1.next, l2.next
#             elif l2 and not l1:
#                 sum += l2.val
#                 l2 = l2.next
#             elif l1 and not l2:
#                 sum += l1.val
#                 l1 = l1.next
            
#             curr = ListNode(sum % 10)
#             prev.next = curr
#             prev = curr
#             sum = sum // 10
#         return head.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """
        sum = 0
        head = ListNode()
        prev = head
        while l1 or l2 or sum:
            
            sum = sum + l1.val if l1 else sum
            sum = sum + l2.val if l2 else sum
            
            curr = ListNode(sum % 10)
            prev.next = curr
            prev = curr
            sum = sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next


l1 = [1,2,3]
l2 = [4,5,6]

# l1 = [9]
# l2 = [9]

l1 = ListNode.listToNodes(l1)
l2 = ListNode.listToNodes(l2)

x = Solution()
print(x.addTwoNumbers(l1,l2))