#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find length
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next

        # nth from end is l -n from head
        pos = i - n

        # if we need to remove 0th
        if pos == 0:
            return head.next

        # if we need to remove first or further
        i = 0
        curr = head
        while i + 1 < pos:
            curr = curr.next
            i += 1

        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return head
            
        


"""
Input: head = [1,2,3,4], n = 2

Output: [1,2,4]

"""

s = [1,2,3,4]
n = 2

# s = [5] 
# n = 1

s = [1,2]
n = 2

data = [
    {
        's': [1,2],
        'n': 1
    },
    {
        's': [1,2,3,4],
        'n': 2
    },
    {
        's': [5],
        'n': 1
    },
    {
        's': [1,2],
        'n': 2
    },
]

for i in data:
    s, n = i['s'], i['n']
    head = ListNode(s[0])
    prev = head
    for i in range(1,len(s)):
        curr = ListNode(s[i])
        prev.next = curr
        prev = curr

    x = Solution()
    print(s, n, x.removeNthFromEnd(head, n))