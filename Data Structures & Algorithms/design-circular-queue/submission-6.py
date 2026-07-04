class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.space_available = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        else:
            self.head = Node(value)
            self.tail = self.head
        self.space_available -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head and self.head.next:
            self.head = self.head.next
        elif self.head:
            self.head = None
            self.tail = None
        self.space_available += 1
        return True

    def Front(self) -> int:
        if self.head:
            return self.head.val
        return -1

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.head is None

    def isFull(self) -> bool:
        return self.space_available == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()