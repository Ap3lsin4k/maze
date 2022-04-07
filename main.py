from typing import Sequence, Tuple


def copy_and_mark_walls(maze):
    return [[-cell for cell in row] for row in maze]


def find_distance(maze: Sequence[Sequence], i=0, j=0):
    dist = copy_and_mark_walls(maze)
    return _find_distance(maze, dist, (i, j))


def _find_distance(maze, dist, starting_point: Tuple[int, int]):
    queue = [starting_point]
    visited = set()
    distance = 0

    def move(i, j):

        def is_empty():
            if i < 0 or j < 0:
                return False
            try:
                return maze[i][j] == 0
            except IndexError:
                return False

        def is_visited():
            return dist[i][j] or is_starting_point()

        def is_starting_point():
            return i == starting_point[0] and j == starting_point[1]

        if is_empty() and not is_visited():
            dist[i][j] = distance
            queue.append((i, j))
            visited.add((i, j))

    while queue:
        i, j = queue.pop(0)
        distance += 1

        move(i, j + 1)
        move(i + 1, j)
        move(i, j - 1)
        move(i - 1, j)

    return dist
