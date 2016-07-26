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
from collections import namedtuple

import pytest

Tree = namedtuple('Tree', 'x l r')


def is_balanced(T):
    """
    Time: O(n log n), Space worst O(n) best/avg O(log n)
    """
    if T is None:
        return True

    diff_height = abs(height(T.l) - height(T.r))

    if diff_height > 1:
        return False

    if not is_balanced(T.l) or not is_balanced(T.r):
        return False

    return True


def height(T):
    """
    Time O(n), Space worst O(n) best/avg O(log n)
    """
    if T is None:
        return 0

    return max(height(T.l), height(T.r)) + 1


def improved_is_balanced(T):
    """
    Time O(n), Space worst O(n) best/avg O(log n)
    """
    if T is None:
        return True
    if improved_height(T) == -1:
        return False
    return True


def improved_height(T):
    """
    Returns -1 if tree is not balanced, returns the height of the tree otherwise.
    Time O(n), Space worst O(n) best/avg O(log n)
    """
    if T is None:
        return 0

    left_h = improved_height(T.l)
    if left_h == -1:
        return -1

    right_h = improved_height(T.r)
    if right_h == -1:
        return -1

    if abs(left_h - right_h) > 1:
        return -1

    return max(left_h, right_h) + 1


BALANCED = Tree(10,
                Tree(1,
                     Tree(2, None, None),
                     Tree(6, None, None)),
                Tree(15,
                     Tree(16, None,
                          Tree(3, None, None)),
                     Tree(3, None, None)))

NOT_BALANCED = Tree(10,
                    Tree(1,
                         Tree(2,
                              Tree(4,
                                   Tree(19, None, None),
                                   None),
                              Tree(8, None, None)),
                         Tree(7, None, None)),
                    None)


@pytest.mark.parametrize('input, expected', [
    (BALANCED, True),
    (NOT_BALANCED, False)
])
def test_is_balanced(input, expected):
    assert is_balanced(input) is expected


@pytest.mark.parametrize('input, expected', [
    (BALANCED, True),
    (NOT_BALANCED, False)
])
def test_improved_is_balanced(input, expected):
    assert improved_is_balanced(input) is expected
