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


def rotate_right(matrix):
    if not matrix:
        return

    end = len(matrix) - 1
    start = 0

    while start < end:
        for i in range(end - start):
            left = matrix[end - i][start]
            # bottom to left
            matrix[end - i][start] = matrix[end][end - i]
            # right to bottom
            matrix[end][end - i] = matrix[start + i][end]
            # top to right
            matrix[start + i][end] = matrix[start][start + i]
            # left to top
            matrix[start][start + i] = left
        end -= 1
        start += 1
    return matrix


@pytest.mark.parametrize('input, expected', [
    (None, None),
    ([[1, 2],
      [3, 4]], [[3, 1],
                [4, 2]]),
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]], [[7, 4, 1],
                   [8, 5, 2],
                   [9, 6, 3]]),
    ([[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]], [[13, 9, 5, 1],
                          [14, 10, 6, 2],
                          [15, 11, 7, 3],
                          [16, 12, 8, 4]])
])
def test_rotate_right(input, expected):
    assert rotate_right(input) == expected
