class MyHashSet:

    def __init__(self):
        self.hash_set = [0] * 31251

    def add(self, key: int) -> None:
        self.hash_set[key // 32] |= 1 << (key % 32)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash_set[key // 32] ^= 1 << (key % 32)

    def contains(self, key: int) -> bool:
        return (self.hash_set[key // 32] & (1 << (key % 32))) != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)