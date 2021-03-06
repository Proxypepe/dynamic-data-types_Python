from abc import ABC, abstractmethod


class Tree(ABC):

    @abstractmethod
    def _Tree__add_node(self, tree, value: object):
        pass

    @abstractmethod
    def _Tree__print_inorder(self, tree):
        pass

    @abstractmethod
    def _Tree__print_postorder(self, tree):
        pass

    @abstractmethod
    def _Tree__print_preorder(self, tree):
        pass

    @abstractmethod
    def _Tree__min_node(self, tree):
        pass

    @abstractmethod
    def _Tree__max_node(self, tree):
        pass

    def add_node(self, value: object):
        self._Tree__add_node(self, value)

    def print_inorder(self):
        self._Tree__print_inorder(self)

    def print_postorder(self):
        self._Tree__print_postorder(self)

    def print_preorder(self):
        self._Tree__print_preorder(self)

    def min_node(self):
        self._Tree__min_node(self)

    def max_node(self):
        self._Tree__max_node(self)
