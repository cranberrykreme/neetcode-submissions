class Node:
    def __init__(self, key: int, val: int, counter: int, next = None, prev = None):
        self.key = key
        self.val = val
        self.counter = counter
        self.next = next
        self.prev = prev

class LFUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.head = Node(0, 0, -1)
        self.tail = Node(0, 0, float('inf'))
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        node.counter += 1

        while node.next and node.next.counter <= node.counter:
            old_prev = node.prev
            old_next = node.next
            old_next_next = old_next.next
            old_next.prev, old_next.next = old_prev, node
            old_prev.next = old_next
            node.next, node.prev = old_next_next, node.next
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            self.nodes[key].val = value
            self.get(key)
            return
        
        if self.capacity == len(self.nodes):
            to_remove = self.head.next
            self.head.next = to_remove.next
            to_remove.next.prev = self.head
            del self.nodes[to_remove.key]
        
        to_add = Node(key, value, 0, self.head.next, self.head)
        self.nodes[key] = to_add

        self.head.next = to_add
        to_add.next.prev = to_add
        self.get(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)