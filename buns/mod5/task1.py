class ListNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.root = None


class Stack:
    def __init__(self, values=None):
        self.__values = SinglyLinkedList()
        self.__len = 0
        if values is not None:
            for v in values:
                self.add(v)
    
    def add(self, value):
        self.__len += 1
        if self.__values.root is None:
            self.__values.root = ListNode(value)
            return
        new_node = ListNode(value)
        new_node.next_node = self.__values.root
        self.__values.root = new_node

    def pop(self):
        if self.__values.root is None:
            raise IndexError("pop from an empty stack")
        root = self.__values.root
        self.__values.root = self.__values.root.next_node
        self.__len -= 1
        return root.value

    def __len__(self):
        return self.__len

    def __iter__(self):
        cur = self.__values.root
        while cur is not None:
            yield cur.value
            cur = cur.next_node
