#!/usr/bin/env python

# Definition for singly-linked list.
from typing import Optional
from Node import Node
    


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodes = {None: None}
        while curr:
            new_node = Node(curr.val)
            nodes[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            new_node = nodes[curr]
            new_node.random = nodes[curr.random]
            new_node.next = nodes[curr.next]
            curr = curr.next
        return nodes[head]







s = [[3,None],[7,3],[4,0],[5,1]]


head = Node(s[0][0])
prev = head
for i in range(1,len(s)):
    curr = Node(s[i][0])
    prev.next = curr
    prev = curr

x = Solution()
print(x.copyRandomList(head=head))
