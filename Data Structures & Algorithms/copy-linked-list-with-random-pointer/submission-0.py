"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(0)
        curr = head
        new_curr = new_head
        new_nodes = {None: None}
        while curr:
            copy = Node(curr.val)
            new_nodes[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = new_nodes[curr]
            copy.next = new_nodes[curr.next]
            copy.random = new_nodes[curr.random]
            curr = curr.next
        return new_nodes[head]