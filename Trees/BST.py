from Tree import Tree


class BST(Tree):

    def __init__(self, value: object):
        self.__value = value
        self.__left = None
        self.__right = None

    def _Tree__add_node(self, tree, value: object):
        if tree is None:
            tree = BST(value)
            return tree
        elif tree.__value > value:
            tree.__left = self._Tree__add_node(tree.__left, value)
        else:
            tree.__right = self._Tree__add_node(tree.__right, value)

        return tree

    def _Tree__print_inorder(self, v):
        if v is None:
            return
        self._Tree__print_inorder(v.__left)
        print(f"value: {v.__value}")
        self._Tree__print_inorder(v.__right)

    def _Tree__print_postorder(self, v):
        if v is None:
            return
        self._Tree__print_postorder(v.__left)
        self._Tree__print_postorder(v.__right)
        print(f"value: {self.__value}")

    def _Tree__print_preorder(self, v):
        if v is None:
            return
        print(f"value: {self.__value}")
        self._Tree__print_preorder(v.__left)
        self._Tree__print_preorder(v.__right)

    def _Tree__min_node(self, v):
        if v.__left is None:
            return v.__value
        self._Tree__min_node(v.__left)

    def _Tree__max_node(self, v):
        if v.__right is None:
            return v.__value
        self._Tree__max_node(v.__right)

    def _Tree__find(self, v,  value):
        res1 = None
        res2 = None
        if v is None:
            return False
        if v.__value == value:
            return True
        if v.__value > value:
            res1 = self._Tree__find(v.__left, value)
        elif v.__value < value:
            res2 = self._Tree__find(v.__right, value)
        if res1:
            return True
        if res2:
            return True
