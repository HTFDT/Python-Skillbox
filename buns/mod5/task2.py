class ListNode:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    def __init__(self):
        self.first = self.last = None


class Queue:
    def __init__(self, values=None):
        self.__len = 0
        self.__values = LinkedList()
        if values is not None:
            for v in values:
                self.add(v)

    def add(self, value):
        self.__len += 1
        if self.__values.first is None:
            self.__values.first = self.__values.last = ListNode(value)
            return
        new_node = ListNode(value)
        self.__values.last.next_node = new_node
        new_node.prev_node = self.__values.last
        self.__values.last = new_node

    def pop(self):
        if self.__values.first is None:
            raise IndexError("pop from an empty queue")
        self.__len -= 1
        if self.__values.first == self.__values.last:
            val = self.__values.first.value
            self.__values.first = self.__values.last = None
            return val
        first = self.__values.first
        self.__values.first = self.__values.first.next_node
        self.__values.first.prev_node = None
        return first.value
    
    def __len__(self):
        return self.__len
    
    def __iter__(self):
        cur = self.__values.first
        while cur is not None:
            yield cur.value
            cur = cur.next_node
