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
