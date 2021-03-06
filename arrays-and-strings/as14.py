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


def replace_space(array_string, length):
    """
    Time: O(n) Space: O(1)
    """
    if length == 0:
        return array_string
    counter = 0
    for i in range(length):
        if array_string[i] == ' ':
            counter += 1

    current_idx = -1
    for i in reversed(range(length)):
        if counter == 0:
            break
        if array_string[i] != ' ':
            array_string[current_idx] = array_string[i]
            current_idx -= 1
        else:
            array_string[current_idx - 2:current_idx + 1] = ['%', '2', '0']
            counter -= 1
            current_idx -= 3
    return array_string


@pytest.mark.parametrize('input, expected', [
    ((['h', 'o', 'l', 'a', ' ', 'c', 'o', 'm', 'o', ' ', 'e', 's', 't', 'a', 's', '?', ' ', ' ', ' ', ' '], 16),
     ['h', 'o', 'l', 'a', '%', '2', '0', 'c', 'o', 'm', 'o', '%', '2', '0', 'e', 's', 't', 'a', 's', '?']),
    (([' ', 'a', 'b', 'c', ' ', ' '], 4), ['%', '2', '0', 'a', 'b', 'c']),
    (([], 0), [])
])
def test_replace_spaces(input, expected):
    assert replace_space(*input) == expected
