# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans_head = ans
        while list1 != None and list2 != None:
            if list2.val < list1.val:
                ans.next = list2
                list2 = list2.next
            else:
                ans.next = list1
                list1 = list1.next
            ans = ans.next
        if list1 != None:
            ans.next = list1
        if list2 != None:
            ans.next = list2
        return ans_head.next