from collections import deque

import pytest


class Node:
    def __init__(self, num, adj=None):
        self.num = num
        self.adj = [] if adj is None else adj
        self.visited = False


def has_path_dfs(nodeA, nodeB):
    """
    Depth-first-search
    Time: O(num) Space: O(num)
    :param nodeA:
    :param nodeB:
    :return:
    """
    if nodeA is None or nodeB is None:
        return False

    nodeA.visited = True

    for node in nodeA.adj:
        if not node.visited and (node == nodeB or has_path_dfs(node, nodeB)):
            return True

    return False


def has_path_bfs(nodeA, nodeB):
    """
    Breath-first-search
    Time: O(num) Space: O(num)
    :param nodeA:
    :param nodeB:
    :return:
    """
    if nodeA is None or nodeB is None:
        return False

    queue = deque()

    nodeA.visited = True
    queue.appendleft(nodeA)

    while len(queue) > 0:
        node = queue.pop()
        for n in node.adj:
            if n == nodeB:
                return True
            if not n.visited:
                n.visited = True
                queue.appendleft(n)

    return False


G = Node(6)
F = Node(5, [G])
E = Node(4, [F])
D = Node(3, [E, F])
C = Node(2, [D, E])
B = Node(1, [D])
A = Node(0, [B, C])
F.adj.append(C)


@pytest.fixture(autouse=True)
def reset_visited():
    for node in [A, B, C, D, E, F, G]:
        node.visited = False


@pytest.mark.parametrize('nodeA,nodeB,expected', [
    (A, G, True),
    (B, C, True),
    (C, B, False)
])
def test_has_path_dfs(nodeA, nodeB, expected):
    assert has_path_dfs(nodeA, nodeB) is expected


@pytest.mark.parametrize('nodeA,nodeB,expected', [
    (A, G, True),
    (B, C, True),
    (C, B, False)])
def test_has_path_bfs(nodeA, nodeB, expected):
    assert has_path_bfs(nodeA, nodeB) is expected
