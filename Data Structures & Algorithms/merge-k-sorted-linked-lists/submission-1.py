# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head
        min_heap = []
        for i, lst in enumerate(lists):
            if lst is not None:
                heapq.heappush(min_heap, (lst.val, i, lst))
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            curr.next = node
            curr = node
            node = node.next

            if node is not None:
                heapq.heappush(min_heap, (node.val, i, node))
        return dummy_head.next