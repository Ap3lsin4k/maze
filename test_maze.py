from main import find_distance, copy_and_mark_walls


def test_maze():
    assert find_distance([[0, 0]]) == [[0, 1], ], find_distance([[0, 0]])

    assert find_distance([[0, 0], [0]]) == [[0, 1], [1]], find_distance([[0, 0, 0]])
    assert find_distance([[0, 0]], 0, 1) == [[1, 0]]


def test_different_starting_point():
    assert find_distance([[0],
                          [0]], 1, 0) == [[1],
                                          [0]]


def test_2_by_2_with_shape_l():
    square = [[0],
              [0, 0]]
    assert find_distance(square, 0, 0) == [
        [0],
        [1, 2],
    ]


def test_2_by_2_empty_square():
    square = [[0, 0],
              [0, 0]]
    assert find_distance(square, 0, 0) == [
        [0, 1],
        [1, 2],
    ]


def test_1_by_1():
    assert find_distance([[0]], 0, 0) == [[0]]


def test_walls():
    actual = [[0, 1]]
    assert copy_and_mark_walls(actual) == [[0, -1]]
    assert find_distance(actual, 0, 0) == [[0, -1]]


def test_create_copy_of_maze_and_fill_with_zeroes():
    maze = [[0, 1], [1, 1]]
    dist = copy_and_mark_walls(maze)
    dist[0][0] = 'a'

    assert dist == [['a', -1], [-1, -1]], dist


def test_unreachable():
    actual = [[0, 1, 0]]

    assert find_distance(actual, 0, 0) == [[0, -1, 0]]
