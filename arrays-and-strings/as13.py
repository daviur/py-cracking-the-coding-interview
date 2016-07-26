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
