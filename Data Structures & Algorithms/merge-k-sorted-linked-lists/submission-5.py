# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        k = len(lists)
        gap = 1
        while gap < k:
            for i in range(0, k, gap*2):
                dummy_head.next = None
                curr = dummy_head
                l1 = lists[i]
                l2 = None
                if i+gap < k:
                    l2 = lists[i+gap]

                while l1 and l2:
                    node = l1
                    if l2.val < l1.val:
                        node = l2
                        l2 = l2.next
                    else:
                        l1 = l1.next
                    curr.next = node
                    curr = curr.next
                
                curr.next = l1 if l1 else l2
                lists[i] = dummy_head.next
            gap *= 2
        return lists[0] if k > 0 else None
