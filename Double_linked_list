from Linked_list import Linked_list

class Node:
    def __init__(self, value: object) -> object:
        self._next = None 
        self._tail = Node
        self._value = value

class double_list(Linked_list):
    
    def __init__(self):
        self.__head = None  
        self.__tail = None 

    def push_back(self, value :object):
        if self.__head == None and self.__tail == None:
            self.__head = self.__tail = Node(value)
        else:
            _tmp = Node(value)
            _tmp.__tail = self.__tail
            self.__tail._next = _tmp
            self.__tail = _tmp
          
    
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
        pass
    
    def __str__(self):
        #TODO
        pass

    def print_list(self) -> None:
        q = self.__head
        #print(type(q))
        while(q is not None):
            print(q._value)
            q = q._next
        
