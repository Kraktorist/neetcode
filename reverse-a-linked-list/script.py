from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        node = head
        while node:
            temp = node.next
            node.next = prev_node
            prev_node = node
            node = temp
        return prev_node
    

head = [0,1,2,3]

node = None
for i in head[::-1]:
    node = ListNode(i, node)

x = Solution()

print(x.reverseList(node))