from BST import BST

def main():
    tree = BST(12)
    tree.add_node(13)
    tree.add_node(10)
    tree.print_inorder()

    print(tree.find(10))


if __name__ == '__main__':
    main()
