import Linked_list_abs


class Node:
    def __init__(self, value: object) -> object:
        self._next = None
        self._value = value

class ForwardList(Linked_list_abs.LinkedListAbstract):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__iter = None
        self.__len = 0
        self.__current_position = 0

    def push_back(self, value: object) -> None:
        if self.is_empty():
            self.__head = self.__tail = Node(value)
        else:
            self.__tail._next = Node(value)
            self.__tail = self.__tail._next
        self.__len += 1

    def pop_back(self) -> None:
        if not self.is_empty():
            _tmp = self.__head
            if self.__len == 1:
                del self.__head._next
                self.__head._next = None
                self.__tail = self.__head
            else:
                while _tmp._next._next is not None:
                    _tmp = _tmp._next
                del _tmp._next
                _tmp._next = None
                self.__tail = _tmp
            self.__len -= 1

    def push_front(self, value: object) -> None:
        if self.is_empty():
            self.__head = self.__tail = Node(value)
        else:
            if self.__len == 1:
                _tmp = Node(value)
                _tmp._next = self.__head
                self.__head = _tmp
                self.__tail = self.__head._next
            else:
                _tmp = Node(value)
                _tmp._next = self.__head
                self.__head = _tmp

        self.__len += 1

    def pop_front(self) -> None:
        if not self.is_empty():
            _tmp = self.__head
            self.__head = self.__head._next
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
                for i in range(pos - 2):
                    _q = _q._next
                _tmp._next = _q._next
                _q._next = _tmp
                self.__len += 1

    def insert_after(self, pos: int, value: object) -> None:
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
                _tmp._next = _q._next
                _q._next = _tmp
                self.__len += 1

    def erase(self, pos: int) -> None:
        if not self.is_empty() and pos < self.__len:
            if pos == 0:
                self.pop_front()
            elif pos == self.__len - 1:
                self.pop_back()
            else:
                _q = self.__head
                for i in range(pos - 1):
                    _q = _q._next
                print(f"Value{_q._value}")
                _tmp = _q
                _q._next = _q._next._next
                self.__len -= 1

    def remove(self, element: object) -> None:
        if not self.is_empty():
            _q = self.__head
            while _q._next is not None:
                if _q._next._value == element:
                    if _q._next._next is None:
                        self.pop_back()
                        break
                    else:
                        _tmp = _q._next
                        _q._next = _q._next._next
                        del _tmp
                        self.__len -= 1
                        if _q._next._value != element:
                            _q = _q._next
                else:
                    _q = _q._next

    def is_empty(self) -> bool:
        if self.__head is None:
            return True
        return False

    def __len__(self) -> int:
        return self.__len

    def __iter__(self) -> object:
        self.__iter = self.__head
        self.__current_position = 0
        return self

    def __next__(self) -> object:
        self.__current_position += 1
        if self.__current_position > self.__len:
            raise StopIteration
        now = self.__iter._value
        self.__iter = self.__iter._next
        return now
