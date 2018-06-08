class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = Node()

    def add(self, value):
        new_node = Node(value)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def len(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def insert(self, index, value):
        if index >= self.len():
            self.add(value)
            return
        cur_node = self.head
        cur_index = 0
        while True:
            if cur_index == index:
                prev_node.next = value
                value.next = cur_node
                break
            cur_node = cur_node.next
            cur_index += 1
 
    def get(self, index):
        if index >= self.len():
            raise IndexError
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.value
            cur_idx += 1

    def remove(self, value):
        cur_node = self.head
        if cur_node and cur_node.value == value:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.value != value:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def remove_at(self, index):
        if index >= self.len():
            raise IndexError
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node  = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def clear(self):
        self.__init__()

    def is_empty(self):
        return self.head is None

    def contains(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    



    



