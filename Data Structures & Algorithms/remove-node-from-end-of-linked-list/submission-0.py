# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create dummy node
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Step 2: Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Step 3: Move both pointers until first reaches end
        while first:
            first = first.next
            second = second.next

        # Step 4: Remove nth node
        second.next = second.next.next

        return dummy.next
