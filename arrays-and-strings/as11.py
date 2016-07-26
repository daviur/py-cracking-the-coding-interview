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
import pytest


def unique_characters(string):
    """
    Time: O(n), Space: O(1)
    """
    if len(string) == 0:
        return True

    flags = 0

    for c in string:
        pos = 1 << (ord(c) - ord(' '))
        if flags & pos > 0:
            return False
        flags |= pos

    return True


@pytest.mark.parametrize('input, expected', [
    ('', True),
    ('abcde', True),
    ('aabcd', False),
    ('A' * 9000, False),
    (''.join(chr(i) for i in range(ord(' '), 9000)), True)

])
def test_unique_characters(input, expected):
    assert unique_characters(input) is expected
