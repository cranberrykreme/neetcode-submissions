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
        print(f'getting node.key -> {key}')
        for _, node in self.nodes.items():
            print(f'self.nodes has following keys -> {node.key}')
        if key not in self.nodes:
            print(f'key -> {key} not (NO) in self.nodes')
            return -1
        print(f'key -> {key} is YES in self.nodes')
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
        #print(f'updating node with key -> {node.key}, to tail of counter -> {node.counter}, with next -> {node.next.key}')
        old_next = self._update_old_node_list(node)
        new_list = self.dict_counter_lists.get(node.counter, NodeList())
        #print(f'old_next.key -> {old_next.key}')
        if new_list.tail_node is not None:
            old_next = new_list.tail_node.next
        #print(f'old_next.key -> {old_next.key}')
        #print(f'head.next was previously -> {self.head.next.key}')
        # Update old pointers
        node.prev.next = node.next
        node.next.prev = node.prev
        old_next.prev.next = node

        #print(f'head.next is now -> {self.head.next.key}')
        #print(f'head.next.key -> {self.head.next.key} and its next is -> {self.head.next.next.key}')
        node.next = old_next
        node.prev = old_next.prev
        
        old_next.prev = node
        #print(f'head.next is now -> {self.head.next.key}')
        #node.prev.next = node
        #print(f'node.prev.key -> {node.prev.key}, node.prev.next.key -> {node.prev.next.key}, node.next -> {node.next}')
        #print(f'head.next.key -> {self.head.next.key} and its next is -> {self.head.next.next.key}')
        
        if new_list.head_node == None:
            new_list.head_node = node
        new_list.tail_node = node
        self.dict_counter_lists[node.counter] = new_list
        #print(f'head.next is now -> {self.head.next.key}')
        #print(f'head.next.key -> {self.head.next.key} and its next is -> {self.head.next.next.key}')
    
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
            #print('list_at_idx_one is completely EMPTY')
            node.next = self.head.next
            node.prev = self.head
            node.next.prev = node
            self.head.next = node
            list_at_idx_one.head_node = node
        else:
            #print('list_at_idx_one has values')
            old_tail = list_at_idx_one.tail_node
            node.next = old_tail.next
            node.prev = old_tail
            node.next.prev = node
            old_tail.next = node
        list_at_idx_one.tail_node = node
        self.dict_counter_lists[1] = list_at_idx_one
        #print(f'adding new node.key -> {node.key} with node.next.key -> {node.next.key}, with head.next.key -> {self.head.next.key}')

    def _remove_node(self):
        #print(f'before removal head.next.key -> {self.head.next.key}')
        node_to_remove = self.head.next
        node_list = self.dict_counter_lists.get(node_to_remove.counter, NodeList())
        #print(f'node_list head -> {node_list.head_node.key}, node_list tail -> {node_list.tail_node.key}')
        #for (key, node) in self.nodes.items():
            #print(f'node.key -> {node.key}, node.counter -> {node.counter}')
        if node_list.tail_node == node_to_remove:
            del self.dict_counter_lists[node_to_remove.counter]
            #print(f"deleting node_list, key -> {node_to_remove.key}")
        elif node_list.head_node == node_to_remove:
            node_list.head_node = node_to_remove.next
        
        #print(f'deleting node.key -> {node_to_remove.key}, with node.next.key -> {node_to_remove.next.key}')
        next_node = node_to_remove.next
        next_node.prev = self.head
        self.head.next = next_node
        del self.nodes[node_to_remove.key]
        #print(f'after removing node, head.next -> {self.head.next.key}')


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)