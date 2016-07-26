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
from collections import Counter

import pytest


def is_permutation(string_a, string_b):
    """
    Time: O(n) Space: O(n)
    """
    if string_a is None or string_b is None or len(string_a) != len(string_b):
        return False

    counts = Counter()

    for c in string_a:
        counts[c] += 1

    for c in string_b:
        counts[c] -= 1
        if counts[c] < 0:
            return False
    return True


@pytest.mark.parametrize('input, expected', [
    ((None, 'abc'), False),
    (('abc', None), False),
    (('abcd', 'abc'), False),
    (('abccd', 'abcde'), False),
    (('abcde', 'edcba'), True),
])
def test_is_perutation(input, expected):
    assert is_permutation(*input) is expected
