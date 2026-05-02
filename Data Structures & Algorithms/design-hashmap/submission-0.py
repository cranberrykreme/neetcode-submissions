class Node:
    def __init__(self, key: int, value: int, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hash_map = [Node(0, 0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        node = self.hash_map[self.get_hash(key)]
        while node.next != None and node.next.key != key:
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        node = self.hash_map[self.get_hash(key)]
        while node.next != None:
            node = node.next
            if node.key == key:
                return node.value
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return
        node = self.hash_map[self.get_hash(key)]
        while node.next != None:
            if node.next.key == key:
                node.next = node.next.next
                return


    def get_hash(self, key: int) -> int:
        return key % 10000

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)