# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()   # placeholder head
        current = dummy
        carry = 0

        # iterate while either list has nodes or carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # sum digits + carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # create new node
            current.next = ListNode(digit)
            current = current.next

            # advance lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        