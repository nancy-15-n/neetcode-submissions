# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next      # Save next node
            curr.next = prev     # Reverse the link
            prev = curr          # Move prev forward
            curr = nxt           # Move curr forward
        
        return prev  # New head of reversed list
