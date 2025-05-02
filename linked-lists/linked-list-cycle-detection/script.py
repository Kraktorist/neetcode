# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lp, rp = head, head
        while rp:
            rp = rp.next
            if lp == rp:
                return True
            if rp.next is None:
                return False
            rp = rp.next
            lp = lp.next
        return False
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lp, rp = head, head
        while rp is not None and rp.next:
            rp = rp.next
            if lp == rp:
                return True
            rp = rp.next
            lp = lp.next
        return False