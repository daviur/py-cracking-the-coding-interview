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
