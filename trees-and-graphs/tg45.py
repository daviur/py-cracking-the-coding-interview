import sys
from collections import namedtuple

import pytest

Tree = namedtuple('Tree', 'x l r')

last = None


def is_binary_search_tree_without_duplicates(T):
    """
    Assuming not duplicates.
    Time: O(num), Space: O(log num)
    """
    if T is None:
        return True

    if not is_binary_search_tree_without_duplicates(T.l):
        return False

    global last
    if last != None and T.x <= last:
        return False

    last = T.x

    if not is_binary_search_tree_without_duplicates(T.r):
        return False

    return True


def is_binary_search_tree_with_duplicates(T, min=-sys.maxsize, max=sys.maxsize):
    """
    Min-Max idea.
    Time: O(num) Space: O(log num)
    """
    if T is None:
        return True

    if not min < T.x <= max:
        return False

    if not is_binary_search_tree_with_duplicates(T.l, min, T.x):
        return False

    return is_binary_search_tree_with_duplicates(T.r, T.x, max)


NO_BST = Tree(10,
              Tree(1,
                   Tree(2,
                        Tree(4,
                             Tree(19, None, None),
                             None),
                        Tree(8, None, None)),
                   Tree(7, None, None)),
              Tree(15,
                   Tree(16, None,
                        Tree(3, None, None)),
                   None))

BST = Tree(7,
           Tree(5,
                Tree(3,
                     Tree(2,
                          Tree(1, None, None),
                          None),
                     Tree(4, None, None)),
                Tree(6, None, None)),
           Tree(10,
                Tree(8, None,
                     Tree(9, None, None)),
                None))

BST2 = Tree(20,
            Tree(20, None, None),
            None)

NO_BST2 = Tree(20, None,
               Tree(20, None, None))

NO_BST3 = Tree(7,
               Tree(5,
                    Tree(3,
                         Tree(2,
                              Tree(1, None, None),
                              None),
                         Tree(4, None, None)),
                    Tree(6, None, None)),
               Tree(10, None,
                    Tree(11, None,
                         Tree(9, None, None))))


@pytest.mark.parametrize('tree,expected', [
    (BST, True),
    (BST2, False),
    (NO_BST, False),
    (NO_BST2, False),
    (NO_BST3, False),
])
def test_is_binary_search_tree_without_duplicates(tree, expected):
    assert is_binary_search_tree_without_duplicates(tree) is expected


@pytest.mark.parametrize('tree,expected', [
    (BST, True),
    (BST2, True),
    (NO_BST, False),
    (NO_BST2, False),
    (NO_BST3, False),
])
def test_is_binary_search_tree_with_duplicates(tree, expected):
    assert is_binary_search_tree_with_duplicates(tree) is expected
