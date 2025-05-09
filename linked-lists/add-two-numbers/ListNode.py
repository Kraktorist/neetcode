# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def listToNodes(l):
        head = ListNode(l[0])
        prev = head
        for i in range(1,len(l)):
            curr = ListNode(l[i])
            prev.next = curr
            prev = curr
        return head

    def __repr__(self):
        res = str(self.val)
        nxt = self.next
        i = 0
        while i < 6 and nxt:
            res += f"->{ nxt.val }"
            nxt = nxt.next
            i += 1 
        return res