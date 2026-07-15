# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        prev = dummy_head
        curr = None
        length = 0
        for list in lists:
            curr = list
            while curr is not None:
                length += 1
                curr = curr.next
        print(length)
        count = 0
        while count < length:
            count += 1
            curr_min, idx = float("inf"), -1
            for i, list in enumerate(lists):
                if list and list.val < curr_min:
                    curr_min = list.val
                    idx = i
            curr = lists[idx]
            lists[idx] = lists[idx].next
            prev.next = curr
            prev = curr
            curr = None
        return dummy_head.next