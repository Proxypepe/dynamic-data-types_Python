############
# Linked list  Abstract class
############
from abc import ABC, abstractmethod
    
class LinkedListAbstract(ABC):

    @abstractmethod
    def push_back(self, value: object) -> None:
        """
        Adds an element to the end of the linked list
        :param value: object
        :return: None
        """
        pass

    @abstractmethod 
    def pop_back(self) -> None:
        """
        Removes an element from the end of the linked list
        :return: None
        """
        pass

    def emplace_back(self, *values: iter) -> None:
        """
        Adds an element/ elements to the end of the linked list
        :param values: iter
        :return: None
        """
        for value in values:
            self.push_back(value)

    @abstractmethod
    def push_front(self, value: object) -> None:
        """
        Adds an element to the beginning of the linked list
        :param value: object
        :return: None
        """
        pass

    @abstractmethod
    def pop_front(self) -> None:
        """
        Removes an element from the beginning of the linked list
        :return: None
        """
        pass

    def emplace_front(self, *values: iter) -> None:
        """
        Adds an element/ elements to the beginning of the linked list
        :param values: iter
        :return: None
        """
        for value in values:
            self.push_front(value)

    @abstractmethod
    def insert_before(self, pos: int, value: object) -> None:
        """
        Inserts an element before a given position
        :param pos: int
        :param value: object
        :return: None
        """
        pass

    def emplace_before(self, pos: int,  *values: iter) -> None:
        """
        Inserts an element/ elements before a given position
        :param pos: int
        :param values: iter
        :return: None
        """
        for value in values:
            self.insert_before(pos, value)

    @abstractmethod
    def insert_after(self, pos: int, value: object) -> None:
        """
        Inserts an element after a given position
        :param pos: int
        :param value: object
        :return: None
        """
        pass

    def emplace_after(self, pos: int,  *values: iter) -> None:
        """
        Inserts an element/ elements after a given position
        :param pos: int
        :param values: iter
        :return: None
        """
        for value in values:
            self.insert_after(pos, value)

    @abstractmethod
    def erase(self, pos: int) -> None:
        """
        Removes an element from a given position
        :param pos: int
        :return: None
        """
        pass

    @abstractmethod
    def remove(self, element: object) -> None:
        """
        Removes elements equal to the given one
        :param element: object
        :return: None
        """
        pass

    def remove_if(self, predicate: callable):
        """
        Removes elements if the condition is met
        :param predicate: callable
        :return: None
        """
        counter = 0
        for i in self:
            if predicate(i):
                self.remove(counter)
            counter += 1

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty
        :return: bool
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> object:
        pass

    @abstractmethod
    def __next__(self) -> object:
        pass
