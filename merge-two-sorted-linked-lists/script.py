class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        if list1 and list2:
            if curr1.val > curr2.val:
                head = curr2
                curr2 = curr2.next
            else:
                head = curr1
                curr1 = curr1.next
        elif curr1:
            head = curr1
            curr1 = curr1.next
        elif curr2:
            head = curr2
            curr2 = curr2.next
        else:
            head = None
            
        curr = head
        while curr1 and curr2: 
            if curr1.val > curr2.val:
                curr.next = curr2
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr1 = curr1.next
            curr = curr.next
        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2
        return head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        node.next = list1 or list2
        return head.next
