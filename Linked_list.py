############
# Linked list  Abstract class
############
from abc import ABC, abstractmethod

class LinkedListAbstract(ABC):

    @abstractmethod
    def push_back(self, value: object) -> None:
        pass

    @abstractmethod 
    def pop_back(self) -> None:
        pass

    def emplace_back(self, *values: iter) -> None:
        for value in values:
            self.push_back(value)

    @abstractmethod
    def push_front(self, value: object) -> None:
        pass

    @abstractmethod
    def pop_front(self) -> None:
        pass

    def emplace_front(self, *values: iter) -> None:
        for value in values:
            self.push_front(value)

    @abstractmethod
    def insert_before(self, pos: int, value: object) -> None:
        pass

    def emplace_before(self, pos: int,  *values: iter) -> None:
        for value in values:
            self.insert_before(pos, value)

    @abstractmethod
    def insert_after(self, pos: int, value: object) -> None:
        pass

    def emplace_after(self, pos: int,  *values: iter) -> None:
        for value in values:
            self.insert_after(pos, value)

    @abstractmethod
    def erase(self, pos: int) -> None:
        pass

    @abstractmethod
    def remove(self, element: object) -> None:
        pass

    def remove_if(self, predicate: callable):
        counter = 0
        for i in self:
            if predicate(i):
                self.remove(counter)
            counter += 1

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
