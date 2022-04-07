from main import find_distance, zero


def test_maze():
    assert find_distance([[0, 0]]) == [[0, 1], ], find_distance([[0, 0]])

    assert find_distance([[0, 0], [0]]) == [[0, 1], [1]], find_distance([[0, 0, 0]])
    assert find_distance([[0, 0]], 0, 1) == [[1, 0]]


def test_different_starting_point():
    assert find_distance([[0],
                          [0]], 1, 0) == [[1],
                                          [0]]


def test_2_by_2():
    square = [[0],
              [0, 0]]
    assert find_distance(square, 0, 0) == [
        [0],
        [1, 2],
    ]
def test_2by():
    square = [[0, 0],
              [0, 0]]
    assert find_distance(square, 0, 0) == [
        [0, 1],
        [1, 2],
    ]


def test_create_copy_of_maze_and_fill_with_zeroes():
    maze = [[0, 2], [3, 4]]
    dist = zero(maze)
    dist[0][0] = 'a'

    assert dist == [['a', 0], [0, 0]], dist


def test_1_by_1():
    assert find_distance([[0]], 0, 0) == [[0]]


def test_walls():
    pass
