import copy
from time import sleep
from typing import Sequence, Tuple


def copy_maze_with_walls(maze):
    return [[-cell for cell in row] for row in maze]


def find_distances(walls: Sequence[Sequence], i=0, j=0) -> Sequence[Sequence[int]]:
    dists = copy_maze_with_walls(walls)
    return _fill_empty_cells_with_distances(dists, (i, j))


def _fill_empty_cells_with_distances(dists, starting_point: Tuple[int, int]):
    def move(down, right):
        def is_empty():
            if i < 0 or j < 0:
                return False
            try:
                return dists[i][j] == 0
            except IndexError:
                return False

        def is_visited():
            return is_starting_point()

        def is_starting_point():
            return i == starting_point[0] and j == starting_point[1]

        i, j = queue[0]
        i += down
        j += right

        if is_empty() and not is_visited():
            dists[i][j] = distance
            queue.append((i, j))

    queue = [starting_point, '|']


    def print_all():
        print(f"step #{distance}:")
        for d in dists:
            frmt = "{:>5}" * len(d)

            print('\t', frmt.format(*d).replace(' 0', ' .'))
        print()

    def print_with_delay():
        for i in range(20):
            print_all()
            sleep(0.07)

    distance = 0
    print_with_delay()
    distance += 1

    while queue:
        move(0, +1)
        move(+1, 0)
        move(0, -1)
        move(-1, 0)

        # move(+1, +1)
        # move(-1, -1)
        # move(+1, -1)
        # move(-1, +1)

        queue.pop(0)
        if queue[0] == '|':
            print_with_delay()

            distance += 1
            queue.pop(0)
            if queue:
                queue.append('|')

    return dists
