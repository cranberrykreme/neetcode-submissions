class Node:
    def __init__(self, key: int, val: int, counter: int, next = None, prev = None):
        self.key = key
        self.val = val
        self.counter = counter
        self.next = next
        self.prev = prev

class NodeList:
    def __init__(self, head_node = None, tail_node = None):
        self.head_node = head_node
        self.tail_node = tail_node

class LFUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.head = Node(0, 0, -1)
        self.tail = Node(0, 0, float('inf'))
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.dict_counter_lists: dict[NodeList] = {} # lists head and tail for each counter index

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        node.counter += 1

        self._insert_node_new_loc(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            self.nodes[key].val = value
            self.get(key)
            return
        
        if self.capacity == len(self.nodes):
            self._remove_node()
        
        self._add_new_node_to_counter_index(Node(key, value, 0))

    ### HELPERS ###
    
    # Insert node into its new position.
    def _insert_node_new_loc(self, node: Node):
        old_next = self._update_old_node_list(node)
        new_list = self.dict_counter_lists.get(node.counter, NodeList())
        if new_list.tail_node is not None:
            old_next = new_list.tail_node.next
        # Update old pointers
        node.prev.next = node.next
        node.next.prev = node.prev
        old_next.prev.next = node

        node.next = old_next
        node.prev = old_next.prev
        
        old_next.prev = node

        if new_list.head_node == None:
            new_list.head_node = node
        new_list.tail_node = node
        self.dict_counter_lists[node.counter] = new_list

    # Update the old node list from the previous counter location
    def _update_old_node_list(self, node: Node):
        old_list = self.dict_counter_lists.get(node.counter-1, NodeList())
        old_next = old_list.tail_node.next
        if old_list.head_node == old_list.tail_node:
            del self.dict_counter_lists[node.counter-1]
        elif node == old_list.head_node:
            old_list.head_node = node.next
        elif node == old_list.tail_node:
            old_list.tail_node = node.prev
        return old_next

    def _add_new_node_to_counter_index(self, node: Node):
        node.counter += 1
        self.nodes[node.key] = node
        list_at_idx_one = self.dict_counter_lists.get(1, NodeList())
        if list_at_idx_one.tail_node == None: # entirely empty
            node.next = self.head.next
            node.prev = self.head
            node.next.prev = node
            self.head.next = node
            list_at_idx_one.head_node = node
        else:
            old_tail = list_at_idx_one.tail_node
            node.next = old_tail.next
            node.prev = old_tail
            node.next.prev = node
            old_tail.next = node
        list_at_idx_one.tail_node = node
        self.dict_counter_lists[1] = list_at_idx_one

    def _remove_node(self):
        node_to_remove = self.head.next
        node_list = self.dict_counter_lists.get(node_to_remove.counter, NodeList())

        if node_list.tail_node == node_to_remove:
            del self.dict_counter_lists[node_to_remove.counter]
        elif node_list.head_node == node_to_remove:
            node_list.head_node = node_to_remove.next
        
        next_node = node_to_remove.next
        next_node.prev = self.head
        self.head.next = next_node
        del self.nodes[node_to_remove.key]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)