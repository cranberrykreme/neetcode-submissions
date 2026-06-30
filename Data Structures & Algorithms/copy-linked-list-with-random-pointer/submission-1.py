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
        new_nodes = collections.defaultdict(lambda: Node(0))
        new_nodes[None] = None
        curr = head
        while curr:
            new_nodes[curr].val = curr.val
            new_nodes[curr].next = new_nodes[curr.next]
            new_nodes[curr].random = new_nodes[curr.random]
            curr = curr.next
        return new_nodes[head]