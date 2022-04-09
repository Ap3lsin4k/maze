Given a matrix (with blocked cells) and a starting point,
find the distance between the starting point
and every other points in the matrix.
0 represent empty spaces
1 represent walls

e.g.:
maze =  0 1 0
        0 0 0
        0 1 0

start (0, 0)
dists -> 0 -1 4
         1  2 3
         2 -1 4

start (1, 1)
dists -> 2 -1 2
         1  0 1
         2 -1 2
