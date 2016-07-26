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

    def __repr__(self):
        return '{}'.format(self.data)

    def __str__(self):
        return self.__repr__()


def cover(root, node):
    if root == None or node == None:
        return False
    if root == node:
        return True

    return cover(root.left, node) or cover(root.right, node)


def get_first_common_ancestor_helper(root, nodeA, nodeB):
    if root == None or nodeA == None or nodeB == None:
        return None

    if root == nodeA or root == nodeB:
        return root

    nodeA_is_on_left = cover(root.left, nodeA)
    nodeB_is_on_left = cover(root.left, nodeB)

    if nodeA_is_on_left != nodeB_is_on_left:
        return root

    side_root = root.left if nodeA_is_on_left else root.right

    return get_first_common_ancestor(side_root, nodeA, nodeB)


def get_first_common_ancestor(root, nodeA, nodeB):
    if not cover(root, nodeA) or not cover(root, nodeB):
        return None
    return get_first_common_ancestor_helper(root, nodeA, nodeB)


A = Tree('A')
B = Tree('B')
C = Tree('C')
D = Tree('D')
E = Tree('E')
F = Tree('F')
G = Tree('G')

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


@pytest.mark.parametrize('input, expected', [
    ((None, A, B), None),
    ((A, None, B), None),
    ((A, A, None), None),
    ((A, A, G), None),
    ((A, B, C), B),
    ((A, E, F), D),
    ((A, B, D), A),
    ((A, E, D), D),
    ((A, B, F), A)
])
def test_get_first_common_ancestor(input, expected):
    assert get_first_common_ancestor(*input) == expected
