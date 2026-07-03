# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = dummy = ListNode(0, head)
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        old_head = curr
        old_prev = prev
        for _ in range(right-left+1):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        old_prev.next = prev
        old_head.next = curr
        return dummy.next
        