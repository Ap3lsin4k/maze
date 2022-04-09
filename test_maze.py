from main import find_distances, copy_maze_with_walls


def test_maze():
    assert find_distances([[0, 0]]) == [[0, 1], ], find_distances([[0, 0]])

    assert find_distances([[0, 0], [0]]) == [[0, 1], [1]], find_distances([[0, 0, 0]])
    assert find_distances([[0, 0]], 0, 1) == [[1, 0]]


def test_different_find_distancesing_point():
    assert find_distances([[0],
                           [0]], 1, 0) == [[1],
                                           [0]]


def test_2_by_2_with_shape_l():
    square = [[0],
              [0, 0]]
    assert find_distances(square, 0, 0) == [
        [0],
        [1, 2],
    ]


def test_2_by_2_empty_square():
    square = [[0, 0],
              [0, 0]]
    assert find_distances(square, 0, 0) == [
        [0, 1],
        [1, 2],
    ]


def test_1_by_1():
    assert find_distances([[0]], 0, 0) == [[0]]


def test_walls():
    actual = [[0, 1]]
    assert copy_maze_with_walls(actual) == [[0, -1]]
    assert find_distances(actual, 0, 0) == [[0, -1]]


def test_create_copy_of_maze_and_fill_with_zeroes():
    maze = [[0, 1], [1, 1]]
    dist = copy_maze_with_walls(maze)
    dist[0][0] = 'a'

    assert dist == [['a', -1], [-1, -1]], dist


def test_unreachable():
    actual = [[0, 1, 0]]

    assert find_distances(actual, 0, 0) == [[0, -1, 0]]


def test_immutable_input():
    find_distances(((0,),))


def test_2_by_3():
    maze = (
        (0, 1, 0),
        (0, 0, 0),
    )

    assert find_distances(maze) == [
        [0, -1, 4],
        [1, 2, 3],
    ]
    assert -True == -1


def test_3_by_3():
    maze = (
        (0, 1, 0),
        (0, 0, 0),
        (0, 1, 0),
    )

    assert find_distances(maze) == [
        [0, -1, 4],
        [1, 2, 3],
        [2, -1, 4],
    ]
    assert -True == -1


def test_5_by_3():
    maze = (
        (0, 1, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0, 0, 0),
    )
    assert find_distances(maze) == [
        [0, -1, 4, 5, 6],
        [1, 2, 3, 4, 5],
        [2, -1, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, -1, 6, 7, 8],
        [5, -1, 7, 8, 9],
    ]


def test_the_secret_maze_wave():
    maze = (
        (1, 0, 1, 0, 0, 1, 1, 1),
        (1, 0, 1, 0, 0, 1, 0,),
        (0, 1, 0, 0, 1, 1, 1,),
    )
    solved = [
        [-1, 0, -1, 4.0, 3.5, -1, -1, -1],
        [-1, 1.0, -1, 2.5, 4.0, -1, 0],
        [1.5, -1, 1.5, 3.0, -1, -1, -1]
    ]

    assert find_distances(maze, 0, 1) == solved


def test_demo_rect():
    maze = (
        (0, 1, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 1, 0, 0, 0, 0),
        (0, 1, 1, 1, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 1, 1, 1, 0, 0),
        (0, 1, 1, 0, 1, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 1, 0, 1, 1, 1, 1, 0, 0, 0),
        (0, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    )

    find_distances(maze)