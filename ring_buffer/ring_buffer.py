from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            removed_node = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if removed_node == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        list_buffer_contents.append(self.current.value)

        if self.current == self.storage.tail:
            node = self.storage.head
        else:
            node = self.current.next

        while node is not self.current:
            list_buffer_contents.append(node.value)
            node = node.next if node.next else self.storage.head

        return list_buffer_contents

       # DDL is a good choice as it makes it easier to add and remove data from store due to access from two ends (Head and tail).

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.storage = [None] * capacity

    def append(self, item):
        self.current += 1
        if self.current > len(self.storage) - 1:
            self.current = 0
        self.storage[self.current] = item

    def get(self):
        return [elem for elem in self.storage if elem]
