# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        one = l1
        two = l2
        carry = 0
        new_list = dummy
        while one and two:
            val = carry + one.val + two.val
            carry = 0
            if val > 9:
                carry = 1
                val %= 10
            new_list.next = ListNode(val)
            one = one.next
            two = two.next
            new_list = new_list.next
        while one:
            val = carry + one.val
            carry = 0
            if val > 9:
                carry = 1
                val %= 10
            new_list.next = ListNode(val)
            one = one.next
            new_list = new_list.next
        while two:
            val = carry + two.val
            carry = 0
            if val > 9:
                carry = 1
                val %= 10
            new_list.next = ListNode(val)
            two = two.next
            new_list = new_list.next
        if carry:
            new_list.next = ListNode(carry)
            new_list = new_list.next
        return dummy.next