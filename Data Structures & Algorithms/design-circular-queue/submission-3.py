class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail:
            self.tail.next = Node(value,self.head)
            self.tail = self.tail.next
        else:
            self.head = Node(value)
            self.tail = self.head
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.head and self.head.next:
            self.tail.next = self.head.next
            self.head = self.head.next
            self.count -= 1
            return True
        elif self.head:
            self.head = None
            self.tail = None
            self.count = 0
            return True
        return False

    def Front(self) -> int:
        if self.head:
            return self.head.val
        return -1

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()