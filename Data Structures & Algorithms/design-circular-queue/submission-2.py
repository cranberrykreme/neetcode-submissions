class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = Node(0)
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value)
        if self.isEmpty():
            self.head.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head.next = self.head.next.next
        if self.head.next is None:
            self.tail = self.head
        self.capacity += 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.next.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.head.next == None

    def isFull(self) -> bool:
        return self.capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()