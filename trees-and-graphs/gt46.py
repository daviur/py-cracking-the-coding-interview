import pytest


class Tree:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __eq__(self, other):
        if other == None:
            return False
        return self.data == other.data and self.left == other.left \
               and self.right == self.right

    def __repr_(self):
        return '{}'.format(self.data)

    def __str__(self):
        return self.__repr_()


def get_next(node):
    if node == None:
        return None

    if node.right != None:
        return get_left_most(node.right)

    if node.parent == None:
        return None

    while node.parent != None and node != node.parent.left:
        node = node.parent

    if node.parent != None:
        return node.parent

    return None


def get_left_most(node):
    if node == None:
        return None

    while node.left != None:
        node = node.left
    return node


A = Tree('A')
B = Tree('B')
C = Tree('C')
D = Tree('D')
E = Tree('E')
F = Tree('F')

A.left = B
A.right = D
D.parent = A
D.left = E
D.right = F
F.parent = D
E.parent = D
B.parent = A
B.right = C
C.parent = B


@pytest.mark.parametrize('node, expected', [
    (None, None),
    (A, E),
    (E, D),
    (C, A),
    (F, None)
])
def test_get_next(node, expected):
    assert get_next(node) == expected


if __name__ == '__main__':

    node = B
    print(str(node))
    while node != None:
        node = get_next(node)
        print(str(node))
