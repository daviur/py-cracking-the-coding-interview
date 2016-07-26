# The MIT License (MIT)
#
# Copyright (c) 2016 David I Urbina
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from collections import deque

import pytest


class Tree:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __eq__(self, other):
        if other is None:
            return False
        return self.data == other.data and self.left == other.left and self.right == self.right

    def __repr__(self):
        return '{}'.format(self.data)

    def __str__(self):
        return self.__repr__()


def find(node, subnode):
    if node is None or subnode is None:
        return None

    queue = deque()

    queue.append(node)

    while len(queue) > 0:
        node = queue.popleft()

        if node == subnode:
            return node

        if not node.left is None:
            queue.append(node.left)
        if not node.right is None:
            queue.append(node.right)

    return None


def is_subnode(node, subnode):
    return not find(node, subnode) is None


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
    ((A, D), True),
    ((A, G), False)
])
def test_is_subnode(input, expected):
    assert is_subnode(*input) is expected
