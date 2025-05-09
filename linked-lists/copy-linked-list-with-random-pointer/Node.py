# Definition for singly-linked list.
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __repr__(self):
        res = str(self.val)
        nxt = self.next
        i = 0
        while i < 6 and nxt:
            res += f"->{ nxt.val }"
            nxt = nxt.next
            i += 1 
        return res