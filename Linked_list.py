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

    def emplace_back(self, *values: object) -> None:
        for value in values:
            self.push_back(value)

    @abstractmethod
    def push_front(self, value: object) -> None:
        pass

    @abstractmethod
    def pop_front(self) -> None:
        pass

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
