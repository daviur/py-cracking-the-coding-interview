from collections import namedtuple

import pytest

Tree = namedtuple('Tree', 'data left right')


def all_paths_with_sum_n(node, n):
    paths = []
    if node is None:
        return paths

    def all_paths_with_sum_n_helper(node, n, current_path):
        if node is None:
            return

        current_path.append(node.data)

        for i in range(len(current_path)):
            if sum(current_path[i:]) == n:
                paths.append(current_path[i:])

        all_paths_with_sum_n_helper(node.left, n, current_path)
        all_paths_with_sum_n_helper(node.right, n, current_path)

        current_path.pop()

    all_paths_with_sum_n_helper(node, n, [])
    return paths


tree = Tree(10,
            Tree(1,
                 Tree(2,
                      Tree(-1,
                           Tree(11, None, None),
                           None),
                      Tree(10, None, None)),
                 Tree(7,
                      Tree(6, None, None),
                      None)),
            Tree(5,
                 Tree(-2, None,
                      Tree(3, None, None)),
                 None))


@pytest.mark.parametrize('input, expected', [
    ((tree, 13), [[10, 1, 2], [1, 2, -1, 11], [1, 2, 10], [7, 6], [10, 5, -2]]),
    ((tree, 10), [[10], [-1, 11], [10]]),
    ((tree, 5), [[5]]),
    ((tree, 20), []),
    ((None, 1), [])
])
def test_all_paths_with_sum_n(input, expected):
    assert all_paths_with_sum_n(*input) == expected


if __name__ == '__main__':
    paths = all_paths_with_sum_n(tree, 13)

    print(paths)
