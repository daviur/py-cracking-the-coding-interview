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


def compress(string):
    """
    Time: O(n) Space: O(n)
    """
    if len(string) == 0:
        return ''
    result = []
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            result += [string[i], str(count)]
            count = 1
    result += [string[-1], str(count)]
    if len(string) <= len(result):
        return string
    return ''.join(result)


@pytest.mark.parametrize('input, expected', [
    ('', ''),
    ('abcde', 'abcde'),
    ('aaabbccdddde', 'a3b2c2d4e1'),
    ('aaaaabcdefg', 'aaaaabcdefg'),
    ('aaaaaaaaaaaaaaaaaaabccccccccccccccccc', 'a19b1c17')
])
def test_compress(input, expected):
    assert compress(input) == expected
