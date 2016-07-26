from collections import deque
from collections import namedtuple

Tree = namedtuple('Tree', 'x l r')


def breath_first_search(T):
    """
    a.k.a. Level-order traversal
    Time: O(num) Space: O(num)
    """
    sequence = []

    if T.x == None:
        return sequence

    queue = deque()

    queue.append(T)

    while len(queue) > 0:
        node = queue.popleft()
        sequence.append(node.x)
        if node.l:
            queue.append(node.l)
        if node.r:
            queue.append(node.r)

    return sequence


def preorder(T, sequence=None):
    """
    root-left-right
    Time: O(num) Space: O(h) where h worst case = num , best/avg case = log num
    """
    if sequence == None:
        sequence = []

    if T == None:
        return sequence

    sequence.append(T.x)
    sequence = preorder(T.l, sequence)
    sequence = preorder(T.r, sequence)

    return sequence


def inorder(T, sequence=None):
    """
    Inorder traversal of binary search tree give sorted list of elements.
    left-root-right
    Time: O(num) Space: O(h) where h worst case = num , best/avg case = log num
    """
    if sequence == None:
        sequence = []

    if T == None:
        return sequence

    sequence = inorder(T.l, sequence)
    sequence.append(T.x)
    sequence = inorder(T.r, sequence)

    return sequence


def postorder(T, sequence=None):
    """
    left-right-root
    Time: O(num) Space: O(h) where h worst case = num , best/avg case = log num
    """
    if sequence == None:
        sequence = []

    if T == None:
        return sequence

    sequence = postorder(T.l, sequence)
    sequence = postorder(T.r, sequence)
    sequence.append(T.x)

    return sequence


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
               Tree(20, None, None), )


def test_breath_first_search():
    assert breath_first_search(NO_BST) == [10, 1, 15, 2, 7, 16, 4, 8, 3, 19]


def test_preorder():
    assert preorder(NO_BST) == [10, 1, 2, 4, 19, 8, 7, 15, 16, 3]


def test_inorder():
    assert inorder(NO_BST) == [19, 4, 2, 8, 1, 7, 10, 16, 3, 15]


def test_inorder_on_bst():
    assert inorder(BST) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_postorder():
    assert postorder(NO_BST) == [19, 4, 8, 2, 7, 1, 3, 16, 15, 10]
