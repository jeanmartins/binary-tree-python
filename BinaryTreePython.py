class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root

    def insert(self, val):
        if self._root is None:
            self._root = Node(val)
        else:
            self.addNode(val, self._root)

    def addNode(self, val, node):
        if val <= node.data:
            if node.left is not None:
                self.addNode(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self.addNode(val, node.right)
            else:
                node.right = Node(val)

    def traversal(self, in_order=False, pre_order=False, post_order=False):
        # Criação das listas de pré Ordem, em Ordem e Pós Ordem
        self._pre_order = []
        self._in_order = []
        self._post_order = []

        if self._root is not None:
            if in_order:
                self.inOrder(self._root)
            if pre_order:
                self.preOrder(self._root)
            if post_order:
                self.postOrder(self._root)

            print('InOrder: ' + str(self._in_order))
            print('PreOrder: ' + str(self._pre_order))
            print('PostOrder: ' + str(self._post_order))

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            self._in_order.append(node.data)
            self.inOrder(node.right)

    def preOrder(self, node):
        if node is not None:
            self._pre_order.append(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self._post_order.append(node.data)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.insert(7)
    tree.traversal(True, True, True)
