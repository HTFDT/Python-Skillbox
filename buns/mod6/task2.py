class DoubleElement:
    def __init__(self, *lst):
        self.__lst = lst
        self.__cur_index = 0

    def __iter__(self):
        cur_index = 0
        while cur_index < len(self.__lst):
            yield self.__lst[cur_index], None if cur_index + 1 >= len(self.__lst) else self.__lst[cur_index + 1]
            cur_index += 2
