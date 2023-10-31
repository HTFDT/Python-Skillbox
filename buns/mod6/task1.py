class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.__root = None
        self.__len = 0

    def push(self, value):
        self.__len += 1
        if self.__root is None:
            self.__root = Node(value)
            return
        last = self[len(self) - 1]
        last.next_node = Node(value)

    def remove(self, index: int):
        if index < 0 or index + 1 > len(self):
            raise IndexError("index out of range")
        if index == 0:
            self.__root = self.__root.next_node
            return
        item = self[index - 1]
        item.next_node = item.next_node.next_node

    def insert(self, index, val):
        if index < 0 or index > len(self):
            raise IndexError("index out of range")
        if index == 0:
            new_node = Node(val)
            new_node.next_node = self.__root
            self.__root = new_node
            return

        item = self[index - 1]
        new_item = Node(val, item.next_node)
        item.next_node = new_item

    def __getitem__(self, index):
        if index < 0 or index + 1 > len(self):
            raise IndexError("index out of range")
        cur = 0
        cur_node = self.__root
        while cur != index:
            cur += 1
            cur_node = cur_node.next_node
        return cur_node

    def __len__(self):
        return self.__len

    def __iter__(self):
        cur = self.__root
        while cur is not None:
            yield cur.value
            cur = cur.next_node
