class ListNode:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.nodes = {}

    def get(self, key: int) -> int:
        if key in self.nodes:
            used_node = self.nodes[key]
            if used_node.next is self.tail:
                return used_node.val
            used_node.prev.next, used_node.next.prev = used_node.next, used_node.prev
            used_node.next, used_node.prev = self.tail, self.tail.prev
            self.tail.prev, used_node.prev.next = used_node, used_node
            return used_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.get(key)
            return
        self.nodes[key] = ListNode(key, value, self.tail, self.tail.prev)
        self.nodes[key].prev.next = self.nodes[key]
        self.tail.prev = self.nodes[key]
        if self.capacity < len(self.nodes):
            self.nodes.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head