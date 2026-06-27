# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        counter = 0
        while curr != None and counter <= 1000:
            counter += 1
            curr = curr.next

        return False if counter <= 1000 else True