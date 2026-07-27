# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        start = head
        curr = head
        old_end = dummy_head
        count = 0
        while curr:
            count += 1
            if count == k:
                # swap all the nodes
                curr_move = start
                prev = curr.next
                while count > 0:
                    old_next = curr_move.next
                    curr_move.next = prev
                    prev = curr_move
                    curr_move = old_next

                    count -= 1
                old_end.next = prev
                curr = start
                old_end = start
                start = start.next
            
            curr = curr.next
        return dummy_head.next