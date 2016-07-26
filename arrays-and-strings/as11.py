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
