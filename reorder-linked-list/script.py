# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        res = str(self.val)
        nxt = self.next
        i = 0
        while i < 6 and nxt:
            res += f"->{ nxt.val }"
            nxt = nxt.next
            i += 1 
        return res

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the center
        slowp, fastp = head, head.next
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
        
        # reverse second part
        prev, curr = None, slowp.next
        slowp.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge first and second
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head

s = [0, 1, 2, 3, 4, 5, 6]
s = [2,4,6,8,10]

head = ListNode(s[0])
prev = head
for i in range(1,len(s)):
    curr = ListNode(s[i])
    prev.next = curr
    prev = curr

x = Solution()
print(x.reorderList(head=head))
