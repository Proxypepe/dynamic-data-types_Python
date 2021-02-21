from Linked_list import Linked_list

class Node:
    def __init__(self, value: object) -> object:
        self._next = None
        self._tail = None
        self._value = value

class Double_list(Linked_list):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__iter = None
        self.__len  = 0
        self.__currect_position = 0

    def push_back(self, value :object):
        if self.__head == None and self.__tail == None:
            self.__head = self.__tail = Node(value)
            self.__len += 1
        else:
            _tmp = Node(value)
            _tmp.__tail = self.__tail
            self.__tail._next = _tmp
            self.__tail = _tmp
            self.__len += 1

    def pop_back() -> None:
        #TODO
        pass

    def push_front(value: object) -> None:
        #TODO
        pass

    def pop_front() -> None:
        #TODO
        pass

    def __len__(self):
        #TODO
        return self.__len

    def __str__(self):
        #TODO
        pass

    def __iter__(self):
        self.__iter = self.__head
        self.__currect_position = 0
        return self

    def __next__(self):
        self.__currect_position += 1
        if self.__currect_position > self.__len:
            raise StopIteration
        now = self.__iter._value
        self.__iter = self.__iter._next
        return now
