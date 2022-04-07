def zero(maze):
    return [[0 for _ in row] for row in maze]  # deepcopy([[0]*len(maze[0])] * len(maze))


def find_distance(maze, i=0, j=0):
    dist = zero(maze)
    maze[i][j] = 1
    return _find_distance(maze, dist, (i, j))


def _find_distance(maze, dist, ij):

    def _is_empty(i, j):
        if i < 0 or j < 0:
            return False
        try:
            is_empty = maze[i][j] == 0
            starting_point = i == ij[0] and j == ij[1]
            return is_empty
        except IndexError:
            return False
    queue = [ij]
    visited = set()

    def move(i, j):
        if _is_empty(i, j):
            if not dist[i][j]:
                dist[i][j] = distance
                queue.append((i, j))
                visited.add((i, j))
    distance = 0
    try:
        while queue[0]:
            i, j = queue[0]
            distance += 1
            queue.pop(0)

            move(i, j + 1)
            move(i + 1, j)
            move(i, j - 1)
            move(i - 1, j)

    except IndexError:
        return dist

    # move(i + 1, j)
    # move(i, j + 1)
    #
    # return dist
