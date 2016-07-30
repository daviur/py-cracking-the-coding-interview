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


def zero_matrix(matrix):
    """
    Time: O(nm)) Space: O(1)
    """
    first_column_has_zero = any(True for i in range(len(matrix)) if matrix[i][0] == 0)
    first_row_has_zero = any(True for j in range(len(matrix[0])) if matrix[0][j] == 0)

    _check_for_zeros(matrix)
    _zero_matrix_columns(matrix)
    _zero_matrix_rows(matrix)

    if first_column_has_zero:
        _zero_first_column(matrix)
    if first_row_has_zero:
        _zero_first_row(matrix)

    return matrix


def _check_for_zeros(matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0


def _zero_matrix_columns(matrix):
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0


def _zero_matrix_rows(matrix):
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0


def _zero_first_column(matrix):
    for i in range(len(matrix)):
        matrix[i][0] = 0


def _zero_first_row(matrix):
    for j in range(len(matrix[0])):
        matrix[0][j] = 0


@pytest.mark.parametrize('input, expected', [
    ([[0, 1, 1],
      [1, 0, 1],
      [1, 1, 0]], [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]),
    ([[1, 0, 1, 1],
      [1, 1, 1, 1],
      [0, 1, 1, 1]], [[0, 0, 0, 0],
                      [0, 0, 1, 1],
                      [0, 0, 0, 0]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 1]], [[1, 1, 0, 1],
                      [1, 1, 0, 1],
                      [0, 0, 0, 0],
                      [1, 1, 0, 1]]),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]], [[1, 0, 1],
                   [1, 0, 1],
                   [0, 0, 0],
                   [1, 0, 1]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]], [[1, 1, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1]])
])
def test_zero_matrix(input, expected):
    assert zero_matrix(input) == expected
