from Linked_list_abs import LinkedListAbstract


class Node:
    def __init__(self, value: object) -> object:
        self._next = None
        self._value = value

class CircularList(LinkedListAbstract):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__iter = None
        self.__len = 0
        self.__current_position = 0

    def push_back(self, value: object) -> None:
        pass

    def pop_back(self) -> None:
        pass

    def push_front(self, value: object) -> None:
        pass

    def pop_front(self) -> None:
        pass

    def insert_before(self, pos: int, value: object) -> None:
        pass

    def insert_after(self, pos: int, value: object) -> None:
        pass

    def erase(self, pos: int) -> None:
        pass

    def remove(self, element: object) -> None:
        pass

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
