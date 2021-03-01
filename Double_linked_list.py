from Linked_list import LinkedListAbstract

class Node:
    def __init__(self, value: object) -> object:
        self._next = None
        self._prev = None
        self._value = value

class DoubleList(LinkedListAbstract):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__iter = None
        self.__len  = 0
        self.__current_position = 0

    def push_back(self, value: object):
        if self.is_empty():
            self.__head = self.__tail = Node(value)
        else:
            _tmp = Node(value)
            _tmp._prev = self.__tail
            self.__tail._next = _tmp
            self.__tail = _tmp
        self.__len += 1

    def pop_back(self) -> None:
        if not self.is_empty():
            _tmp = self.__tail
            if self.__len == 1:
                self.__head = self.__tail = None
            else:
                self.__tail = self.__tail._prev
                self.__tail._next = None
            del _tmp
            self.__len -= 1

    def push_front(self, value: object) -> None:
        if self.is_empty():
            self.__head = self.__tail = Node(value)
        else:
            _tmp = Node(value)
            _tmp._next = self.__head
            self.__head._prev = _tmp
            self.__head = _tmp
        self.__len += 1

    def pop_front(self) -> None:
        if not self.is_empty():
            _tmp = self.__head
            if self.__len == 1:
                self.__head = self.__tail = None
            else:
                self.__head = self.__head._next
                self.__head._prev = None
            del _tmp
            self.__len -= 1

    def insert_before(self, pos: int, value: object) -> None:
        if pos > self.__len or pos < 1:
            raise IndexError
        else:
            if self.is_empty():
                self.__head = self.__tail = Node(value)
            elif pos == 1:
                self.push_front(value)
            elif pos == self.__len:
                self.push_back(value)
            else:
                _q = self.__head
                _tmp = Node(value)
                _counter = 0
                for i in range(pos - 1):
                    _q = _q._next
                _tmp._next = _q
                _tmp._prev = _q._prev
                _q._prev._next = _tmp
                _q._prev = _tmp
                self.__len += 1

    def insert_after(self, pos: int, value: object):
        if pos > self.__len:
            raise IndexError
        else:
            if self.is_empty():
                self.__head = self.__tail = Node(value)
            if pos == 1 or pos == self.__len:
                self.push_back(value)
            else:
                _q = self.__head
                _tmp = Node(value)
                _counter = 0
                for i in range(pos):
                    _q = _q._next
                _tmp._next = _q
                _tmp._prev = _q._prev
                _q._prev._next = _tmp
                _q._prev = _tmp
                self.__len += 1

    def erase(self, pos: int) -> None:
        pass

    def remove(self, element: object) -> None:
        if not self.is_empty():
            _q = self.__head
            while _q is not None:
                if _q._value == element:
                    if _q._prev is None:
                        _q = _q._next
                        self.pop_front()
                    elif _q._next is None:
                        self.pop_back()
                        break
                    else:
                        _tmp = _q
                        _q._prev._next = _q._next
                        _q._next._prev = _q._prev
                        del _tmp
                        self.__len -= 1
                        _q = _q._next
                else:
                    _q = _q._next


    def is_empty(self) -> bool:
        if self.__head is None and self.__tail is None:
            return True
        return False

    def __len__(self):
        return self.__len

    def __str__(self):
        #TODO
        pass

    def __iter__(self):
        self.__iter = self.__head
        self.__current_position = 0
        return self

    def __next__(self):
        self.__current_position += 1
        if self.__current_position > self.__len:
            raise StopIteration
        now = self.__iter._value
        self.__iter = self.__iter._next
        return now
