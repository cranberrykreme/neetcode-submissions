# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        count = 1
        prev = dummy = ListNode(0, head)
        while curr and count < left:
            prev = curr
            curr = curr.next
            count += 1
        old_head = curr
        old_prev = prev
        while curr and count <= right:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
            count += 1
        old_prev.next = prev
        old_head.next = curr
        return dummy.next
        